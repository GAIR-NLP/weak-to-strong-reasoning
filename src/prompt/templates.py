from .demonstrations import gsm8k_my_llama2_7b_icl_examples, gsm8k_my_gemma_2b_icl_examples, gsm8k_my_gemma_2b_icl_examples1, gsm8k_my_gemma_2b_icl_examples2, gsm8k_my_mistral_7b_icl_examples, math_my_llama2_7b_icl_examples, math_my_gemma_2b_icl_examples, math_my_mistral_7b_icl_examples

Instruction = ""
gsm8k_my_llama2_7b_icl_template: str = Instruction + gsm8k_my_llama2_7b_icl_examples
gsm8k_my_gemma_2b_icl_template: str = Instruction + gsm8k_my_gemma_2b_icl_examples
gsm8k_my_gemma_2b_icl_template1: str = Instruction + gsm8k_my_gemma_2b_icl_examples1
gsm8k_my_gemma_2b_icl_template2: str = Instruction + gsm8k_my_gemma_2b_icl_examples2
gsm8k_my_mistral_7b_icl_template: str = Instruction + gsm8k_my_mistral_7b_icl_examples
math_my_llama2_7b_icl_template: str = Instruction + math_my_llama2_7b_icl_examples
math_my_gemma_2b_icl_template: str = Instruction + math_my_gemma_2b_icl_examples
math_my_mistral_7b_icl_template: str = Instruction + math_my_mistral_7b_icl_examples

templates = {
    "math-single": "",
    'gsm8k_my_llama2_7b_icl': gsm8k_my_llama2_7b_icl_template,
    'gsm8k_my_gemma_2b_icl': gsm8k_my_gemma_2b_icl_template,
    'gsm8k_my_gemma_2b_icl1': gsm8k_my_gemma_2b_icl_template1,
    'gsm8k_my_gemma_2b_icl2': gsm8k_my_gemma_2b_icl_template2,
    'gsm8k_my_mistral_7b_icl': gsm8k_my_mistral_7b_icl_template,
    'math_my_llama2_7b_icl': math_my_llama2_7b_icl_template,
    'math_my_gemma_2b_icl': math_my_gemma_2b_icl_template,
    'math_my_mistral_7b_icl': math_my_mistral_7b_icl_template,
}
