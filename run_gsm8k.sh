# zero-shot
DEVICE=0,1,2,3
ckpts_dir=""
MODEL_NAME="llama2-70b"
MODEL_TYPE="vllm"
PROMPT_TYPE="zero-shot"
DEV_SET="gsm8k"
TEMPLATE_SET="zero_shot"
INSTRUCTION_TYPE="direct"

CUDA_VISIBLE_DEVICES=${DEVICE} python -u -m src.inference --model_dir ${ckpts_dir}/${MODEL_NAME} --output_file_name outputs/${DEV_SET}/${TEMPLATE_SET}/${MODEL_NAME}/${PROMPT_TYPE}/${INSTRUCTION_TYPE}/output.jsonl --model_type ${MODEL_TYPE} --temperature 0 --dev_set ${DEV_SET} --template ${TEMPLATE_SET} --prompt_type ${PROMPT_TYPE} --answer_key "####" --stop "Question" "Answer" --instruction_type ${INSTRUCTION_TYPE}


# few-shot
DEVICE=0,1,2,3
ckpts_dir=""
MODEL_NAME="llama2-70b"
MODEL_TYPE="vllm"
PROMPT_TYPE="few-shot"
DEV_SET="gsm8k"
TEMPLATE_SET="gsm8k_my_llama2_7b_icl"
INSTRUCTION_TYPE="direct"

CUDA_VISIBLE_DEVICES=${DEVICE} python -u -m src.inference --model_dir ${ckpts_dir}/${MODEL_NAME} --output_file_name outputs/${DEV_SET}/${TEMPLATE_SET}/${MODEL_NAME}/${PROMPT_TYPE}/${INSTRUCTION_TYPE}/output.jsonl --model_type ${MODEL_TYPE} --temperature 0 --dev_set ${DEV_SET} --template ${TEMPLATE_SET} --prompt_type ${PROMPT_TYPE} --answer_key "####" --stop "Question" "Answer" --instruction_type ${INSTRUCTION_TYPE}


# temperature sampling
DEVICE=0,1,2,3
ckpts_dir=""
MODEL_NAME="finetuned-llama2-70b"
MODEL_TYPE="vllm"
PROMPT_TYPE="zero-shot"
DEV_SET="gsm8k_train_2"
TEMPLATE_SET="zero_shot"
INSTRUCTION_TYPE="direct"

for ((seed=0; seed<10; seed++))
do
  CUDA_VISIBLE_DEVICES=${DEVICE} python -u -m src.inference --model_dir ${ckpts_dir}/${MODEL_NAME} --output_file_name outputs/${DEV_SET}/${TEMPLATE_SET}/${MODEL_NAME}/${PROMPT_TYPE}/${INSTRUCTION_TYPE}/t1.0/seed${seed}/output.jsonl --model_type ${MODEL_TYPE} --seed ${seed} --temperature 1.0 --dev_set ${DEV_SET} --template ${TEMPLATE_SET} --prompt_type ${PROMPT_TYPE} --answer_key "####" --stop "Question" "Answer" --instruction_type ${INSTRUCTION_TYPE}
done