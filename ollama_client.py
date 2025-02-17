import subprocess

def run_ollama(prompt, model="llama3.1:latest"):
    """Runs Ollama with the extracted text and returns the output."""
    ollama_command = [
        "ollama", "run",
        model,
        prompt
    ]
    
    try:
        result = subprocess.run(ollama_command, capture_output=True, text=True, check=True, encoding='utf-8')
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Error during Ollama execution:", e)
        print("Ollama stderr:", e.stderr)
        return None
