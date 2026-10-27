import os
# import subprocess # Not directly used as we mock execution, but would be here for real GhostScript calls.

# --- AI Simulation ---
def ask_ai(prompt: str) -> str | None:
    """
    Simulates a local AI understanding a request and suggesting a GhostScript command.
    In a real scenario, this would involve an LLM call to generate the command.
    """
    prompt_lower = prompt.lower()
    
    # Example 1: Compress PDF
    if "compress pdf" in prompt_lower or "reduce size" in prompt_lower:
        input_file = "input.pdf" # Assumes input.pdf exists for this demo
        output_file = "output_compressed.pdf"
        # GhostScript command to compress a PDF
        return f"gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dBATCH -sOutputFile={output_file} {input_file}"
    
    # Example 2: Convert PDF to JPEG
    if "convert pdf to jpeg" in prompt_lower or "pdf to image" in prompt_lower:
        input_file = "input.pdf"
        output_file_pattern = "output_%d.jpeg"
        resolution = 300 # Default resolution
        if "high quality" in prompt_lower or "high res" in prompt_lower:
            resolution = 600
        # GhostScript command to convert PDF pages to JPEG images
        return f"gs -sDEVICE=jpeg -o {output_file_pattern} -r{resolution} {input_file}"
        
    # Example 3: Merge PDFs
    if "merge pdfs" in prompt_lower:
        # This is a bit more complex for a simple AI, but we can suggest a template
        # GhostScript command to merge multiple PDFs into one
        return "gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=merged.pdf input1.pdf input2.pdf"

    # Example 4: Extract text (Note: This typically uses pdftotext, not GhostScript)
    if "extract text" in prompt_lower:
        return "pdftotext input.pdf output.txt (Note: requires poppler-utils, not GhostScript for this specific task)"

    return None

# --- Main Terminal Loop ---
def main():
    print("👻 GhostScript AI: Haunted Terminal Experience 👻")
    print("Type 'help' for suggestions, 'exit' to quit.")
    print("-" * 50)

    # Create a dummy input.pdf for demonstration purposes.
    # This allows the example to be self-contained and runnable without
    # needing a real PDF file from the user.
    dummy_pdf_content = b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n2 0 obj<</Type/Pages/Count 0>>endobj\nxref\n0 3\n0000000000 65535 f\n0000000009 00000 n\n0000000053 00000 n\ntrailer<</Size 3/Root 1 0 R>>startxref\n103\n%%EOF"
    try:
        with open("input.pdf", "wb") as f:
            f.write(dummy_pdf_content)
        print("Created dummy 'input.pdf' for demonstration.")
    except IOError as e:
        print(f"Warning: Could not create dummy 'input.pdf': {e}. Please ensure write permissions.")
        print("Some commands might not work as expected without 'input.pdf'.")

    while True:
        try:
            user_input = input("\nGhostAI> ").strip()
            if user_input.lower() == "exit":
                print("Exiting GhostScript AI. Goodbye!")
                break
            elif user_input.lower() == "help":
                print("Try asking things like:")
                print("  - 'compress my pdf file'")
                print("  - 'convert pdf to jpeg high quality'")
                print("  - 'merge these pdfs'")
                print("  - 'extract text from pdf'")
                continue

            suggested_command = ask_ai(user_input) # The "AI" generates the command here

            if suggested_command:
                print(f"\n👻 GhostAI suggests: {suggested_command}")
                confirm = input("Execute this command? (y/N): ").strip().lower()
                if confirm == 'y':
                    print("\n--- Executing command (mock) ---")
                    # In a real application, you would use subprocess.run() to execute
                    # the GhostScript command. For this example, we just print the command
                    # to avoid requiring GhostScript to be installed on the user's system.
                    print(f"Would execute: {suggested_command}")
                    # Example of how to actually run it (requires GhostScript installed):
                    # try:
                    #     result = subprocess.run(suggested_command.split(), check=True, capture_output=True, text=True)
                    #     print("Command output:")
                    #     print(result.stdout)
                    #     if result.stderr:
                    #         print("Command error (stderr):")
                    #         print(result.stderr)
                    # except FileNotFoundError:
                    #     print("Error: GhostScript (gs) not found. Please ensure it's installed and in your PATH.")
                    # except subprocess.CalledProcessError as e:
                    #     print(f"Error executing command: {e}")
                    #     print(f"Stderr: {e.stderr}")
                    #     print(f"Stdout: {e.stdout}")
                    print("--- Mock execution complete ---")
                else:
                    print("Command execution cancelled.")
            else:
                print("👻 GhostAI couldn't understand your request. Please try rephrasing or type 'help'.")
        except KeyboardInterrupt:
            print("\nExiting GhostScript AI. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Clean up the dummy file created for the demonstration
    if os.path.exists("input.pdf"):
        try:
            os.remove("input.pdf")
            print("\nCleaned up dummy 'input.pdf'.")
        except OSError as e:
            print(f"Warning: Could not remove 'input.pdf': {e}")

if __name__ == "__main__":
    main()