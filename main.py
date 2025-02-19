import subprocess
import threading
import time
from llm_axe import OnlineAgent, OllamaChat

def display_splash_screen():
    green_color_code = "\033[92m"
    reset_color_code = "\033[0m"
    splash_art = """
 ██████╗ ██╗     ██╗      █████╗ ███╗   ███╗ █████╗     ███╗   ██╗███████╗████████╗
██╔═══██╗██║     ██║     ██╔══██╗████╗ ████║██╔══██╗    ████╗  ██║██╔════╝╚══██╔══╝
██║   ██║██║     ██║     ███████║██╔████╔██║███████║    ██╔██╗ ██║█████╗     ██║   
██║   ██║██║     ██║     ██╔══██║██║╚██╔╝██║██╔══██║    ██║╚██╗██║██╔══╝     ██║   
╚██████╔╝███████╗███████╗██║  ██║██║ ╚═╝ ██║██║  ██║    ██║ ╚████║███████╗   ██║   
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝        
    """
    print(f"{green_color_code}{splash_art}{reset_color_code}")
    print("Welcome to the Ollama Model Selector and Prompt Processor!\n")

def get_ollama_models():
    """
    Runs 'ollama list' and extracts the list of available models.
    """
    try:
        # Run the 'ollama list' command and capture the output
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, check=True)
        output = result.stdout
        
        # Extract model names from the output (skip the header line)
        models = [line.split()[0] for line in output.splitlines()[1:]]
        return models
    except subprocess.CalledProcessError as e:
        print(f"Error running 'ollama list': {e}")
        return []

def select_model(models):
    """
    Displays a numbered list of models and allows the user to select one.
    """
    if not models:
        print("No models available. Please ensure Ollama is running and models are pulled.")
        return None
    
    print("Available models:")
    for i, model in enumerate(models):
        print(f"{i + 1}. {model}")
    
    while True:
        try:
            choice = int(input("Select a model by number: "))
            if 1 <= choice <= len(models):
                return models[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def get_user_prompt():
    """
    Prompts the user to input their query.
    """
    return input("Enter your prompt: ")

def spinning_loader(stop_event):
    """
    Displays a spinning ASCII loader until the stop_event is set.
    """
    spinner_frames = ["|", "/", "-", "\\"]
    idx = 0
    while not stop_event.is_set():
        print(f"\rProcessing your request... {spinner_frames[idx]}", end="", flush=True)
        idx = (idx + 1) % len(spinner_frames)
        time.sleep(0.1)
    print("\rProcessing complete!          ")  # Clear the spinner and print completion message

def main():
    # Display the splash screen
    display_splash_screen()
    
    # Step 1: Get the list of available models
    models = get_ollama_models()
    
    if not models:
        return  # Exit if no models are available
    
    # Step 2: Let the user select a model
    selected_model = select_model(models)
    
    if not selected_model:
        return  # Exit if no model is selected
    
    # Step 3: Initialize the selected model
    llm = OllamaChat(model=selected_model)
    online_agent = OnlineAgent(llm)
    
    # Step 4: Get the user's prompt
    prompt = get_user_prompt()
    
    # Step 5: Run the prompt through the model
    print("\nProcessing your request...\n")
    
    # Start the spinning loader in a separate thread
    stop_event = threading.Event()
    loader_thread = threading.Thread(target=spinning_loader, args=(stop_event,))
    loader_thread.start()
    
    # Process the prompt
    resp = online_agent.search(prompt)
    
    # Stop the spinning loader
    stop_event.set()
    loader_thread.join()
    
    # Display the response
    print(resp)

if __name__ == "__main__":
    main()