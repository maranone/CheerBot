import time
import argparse
from datetime import datetime, timedelta
from tqdm import tqdm 
from ollama_client import run_ollama
from screenshot import take_screenshot
from ocr import extract_text_from_image
from pets import format_prompt

def parse_arguments():
    parser = argparse.ArgumentParser(description='Productivity Monitor with customizable intervals')
    parser.add_argument(
        '--screenshot-interval', 
        type=int, 
        default=60,
        help='Interval between screenshots in seconds (default: 60)'
    )
    parser.add_argument(
        '--analysis-interval', 
        type=int, 
        default=300,
        help='Interval between showing productivity analysis in seconds (default: 300)'
    )
    parser.add_argument(
        '--debug', 
        action='store_true',  # This makes the argument a boolean flag
        help='Show all prompts (default: False)'
    )
    parser.add_argument(
        '--personality', 
        type=str, 
        choices=['cat', 'dog', 'parrot'], 
        default='cat', 
        help="Choose the personality for prompts (default: 'cat')"
    )
    return parser.parse_args()


def monitor_productivity(screenshot_interval, analysis_interval):
    """
    Continuously monitors productivity with configurable intervals
    
    Args:
        screenshot_interval: Seconds between screenshots
        analysis_interval: Seconds between showing analysis popups
    """
    previous_text = None
    change_history = []
    last_analysis_time = time.time()
    prompts = format_prompt(args.personality)
    
    print(f"Starting productivity monitor:")
    print(f"- Taking screenshots every {screenshot_interval} seconds")
    print(f"- Showing analysis every {analysis_interval} seconds")
    
    try:
        pbar = tqdm(total=screenshot_interval, ncols=100, desc=f"Capturing screenshot", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed} < {remaining}, {rate_fmt}]")
        while True:
            current_time = datetime.now()
            pbar.n = 0
            pbar.last_print_n = 0
            pbar.update(0)

            for _ in range(screenshot_interval):
                time.sleep(1)
                pbar.update(1)
            
            take_screenshot()
            extracted_text = extract_text_from_image()

            if previous_text:
                # Compare with previous screenshot
                previous_time = current_time - timedelta(seconds=screenshot_interval)
                ollama_prompt = prompts["change"].format(
                    time1=previous_time.strftime("%H:%M:%S"),
                    time2=current_time.strftime("%H:%M:%S"),
                    prev_text=previous_text,
                    curr_text=extracted_text
                )
                change_summary = run_ollama(ollama_prompt)
                if change_summary:
                    change_history.append(f"[{current_time.strftime('%H:%M:%S')}] {change_summary}")
                    if args.debug: 
                        print(f"Change detected: {change_summary}")

            previous_text = extracted_text

            # Check if it's time for analysis
            current_timestamp = time.time()
            if current_timestamp - last_analysis_time >= analysis_interval:
                if change_history:
                    final_prompt = prompts["summary"].format(
                        history="\n".join(change_history[-5:])  # Only use last 5 observations
                    )
                    final_response = run_ollama(final_prompt)
                    print(f"\n{prompts['emoji']} Productivity Analysis:", final_response)

                # Reset for next analysis period
                last_analysis_time = current_timestamp
                change_history = []

            time.sleep(screenshot_interval)

    except KeyboardInterrupt:
        pbar.close()
        print("\nProductivity monitoring stopped by user")

if __name__ == "__main__":
    args = parse_arguments()
    monitor_productivity(args.screenshot_interval, args.analysis_interval)
