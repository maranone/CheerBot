Disclaimer
This project does not use any external APIs or any cloud-based services. 
All execution and processing, including text extraction and productivity analysis, happens locally on your machine. 
Your data remains private and secure as no information is sent to external servers.

Productivity Monitor 
A Python-based productivity monitor that captures screenshots at configurable intervals, extracts text from them using OCR, and provides productivity analysis using customizable prompts.

Features
Configurable Intervals: Set the frequency for screenshots and productivity analysis.
OCR Text Extraction: Automatically extracts text from screenshots to track changes.
Customizable Prompts: Use different personalities (cat, dog, parrot) for productivity analysis prompts.
Real-time Monitoring: View live updates of the screenshot capture and analysis.
Analysis History: Keeps track of recent changes and summarizes productivity in intervals.

Requirements
Python 3.x
Dependencies:
tqdm
ollama_client
tesseract

Usage
Command-line Arguments
Argument	Description	Default
--screenshot-interval	Interval between screenshots in seconds.	60
--analysis-interval	Interval between productivity analysis in seconds.	300
--debug	If set, shows all prompts and outputs.	False
--personality	Choose the personality for prompts: cat, dog, or parrot.	cat

Example
To start the productivity monitor with the following options:
Screenshot every 60 seconds.
Show productivity analysis every 300 seconds.
Use the dog personality.
Run the following command:

python productivity_monitor.py --screenshot-interval 60 --analysis-interval 300 --personality dog

How it Works
Screenshot Capture: Screenshots are taken at the interval specified by --screenshot-interval.
Text Extraction: The text from each screenshot is extracted using OCR.
Change Detection: The extracted text is compared with the previous screenshot to detect changes.
Productivity Analysis: Every --analysis-interval seconds, a summary of the most recent changes is provided, based on the last 5 detected changes.
The program uses the ollama_client for generating productivity analysis, with customizable personality prompts (cat, dog, parrot) from the pets module.

Customization
You can modify the text and behavior of the analysis prompts in the pets.py file. It is easy to adjust the text, tone, and structure of the productivity summaries based on your preferences.

Examples with llama3.1:latest 8b (you can change it in ollama_client.py)
Dog Example Output
Starting productivity monitor:
- Taking screenshots every 5 seconds
- Showing analysis every 30 seconds
Capturing screenshot: 100%|█████████████████████████████████████████| 5/5 [00:18 < 00:00,  1.64s/it]
🐶 Productivity Analysis: WOOF WOOF WOOO! Hooman's so close to finishing that project, I just know it! *pant pant* Come on, human, you can do it!
Capturing screenshot: 100%|█████████████████████████████████████████| 5/5 [00:57 < 00:00,  2.02s/it]
🐶 Productivity Analysis: WOOHOO WOOF WOOF! Hooman's working so hard on that computer! You can do it, hooman, create that repository and make all the code changes go "RUFF RUFF" smoothly! *jumps up and down*
Capturing screenshot: 100%|█████████████████████████████████████████| 5/5 [01:33 < 00:00,  2.00s/it]
🐶 Productivity Analysis: I'll just keep an eye on you, hooman! *pant pant* You're doing such great work on CheerBot, I can feel the excitement! GO GO GO, make it the best pet ever, HOOOUMAN! *barks loudly and jumps up with enthusiasm*
Capturing screenshot: 100%|█████████████████████████████████████████| 5/5 [02:08 < 00:00,  2.03s/it]
🐶 Productivity Analysis: WOOF WOOF WOOOOF! Oh boy, oh boy, you're typing away like a machine, Hooman! Can I get a belly rub in between those lines? *bounces up and down*

Cat Example Output
python main.py --screenshot-interval 5 --analysis-interval 30 --personality cat --debug
Starting productivity monitor:
- Taking screenshots every 5 seconds
- Showing analysis every 30 seconds
Capturing screenshot: 100%|█████████████████████████████████████████| 5/5 [00:19 < 00:00,  1.73s/it]Change detected: Here's a single sentence reaction:

"Meh, more games to add to my wishlist, argh, not purr-fectly focused on productivity, but Arken Age does look interesting..."
Capturing screenshot: 100%|█████████████████████████████████████████| 5/5 [00:38 < 00:00,  2.09s/it]Change detected: I think the answer is: "You'd better purr-haps try this game again, human, since it has high praise and you want to give it another go!"

🐱 Productivity Analysis: *stretches languidly* Ahah, finally a spark of feline-approved focus in your eyes, human 🐱💡. You're pouncing on Arken Age with renewed interest, eh? Now don't get too caught up in gaming - I need belly rubs! 😾

Contributing
Feel free to fork the repository and submit pull requests with improvements, bug fixes, or additional features.

License
This project is licensed under the MIT License - see the LICENSE file for details.
