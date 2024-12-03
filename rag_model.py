import torch
import transformers
import shap
import numpy as np

class RAGModel:
    def __init__(self, model_path):
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(model_path)
        self.model = transformers.AutoModelForCausalLM.from_pretrained(model_path)
        
    def generate_response(self, query, context):
        # Combine query and context
        input_text = f"Context: {context}\n\nQuery: {query}\n\nAnswer:"
        
        # Tokenize and generate
        inputs = self.tokenizer(input_text, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=200)
        
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    def explain_model(self, input_text):
        # Use SHAP for model interpretability
        explainer = shap.Explainer(self.model, self.tokenizer)
        shap_values = explainer(input_text)
        
        return shap_values

def main():
    # Example usage
    model_path = "path/to/your/llama/model"  # Replace with actual path
    rag_model = RAGModel(model_path)
    
    context = "Background information about the topic"
    query = "What is your understanding of this context?"
    
    response = rag_model.generate_response(query, context)
    print("Model Response:", response)
    
    # Model Explanation
    explanation = rag_model.explain_model(response)
    print("Model Explanation:", explanation)

if __name__ == "__main__":
    main()