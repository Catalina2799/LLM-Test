from llama_cpp import Llama

MODEL_PATH = "./models/qwen2.5-1.5b-instruct-q4_k_m.gguf"

SYSTEM_PROMPT = ("You are a multilingual translation assistant. Follow the user's instructions and translate accurately while preserving the original meaning and tone.")
print("Loading... this can take a little while the first time.")

model = Llama(model_path = MODEL_PATH, n_ctx = 2038, n_threads = 4, verbose = False)

userInput = input("Hi, I'm your translation assistant. What would you like to ask?\n Type exit to leave \n\n")

while userInput != "exit":
    prompt = [{"role": "system", "content":SYSTEM_PROMPT}, {"role": "user", "content": userInput}]
    result = model.create_chat_completion(prompt, max_tokens=256, temperature = 2)

   # print(result)
    response = result["choices"][0]["message"]["content"]
    print(response)
    userInput = input("You can type exit to leave\n\n")
    print()
print("Good-bye! Thanks for chatting with me!")