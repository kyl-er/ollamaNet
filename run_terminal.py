import subprocess
from llm_axe import OnlineAgent, OllamaChat

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

def main():
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
    resp = online_agent.search(prompt)
    print(resp)

if __name__ == "__main__":
    main()