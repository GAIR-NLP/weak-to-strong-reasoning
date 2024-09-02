# zero-shot
DEVICE=0,1,2,3
splits=("test" "val")
model=""
model_dir=""

for split in ${splits[@]}; do
  CUDA_VISIBLE_DEVICES=${DEVICE} python -u -m src.inference_olympic \
    --split ${split} \
    --stop "Question" "Answer" \
    --model ${model} \
    --model_dir ${model_dir} \
    --output_filename olympic_outputs/${model}/${split}/output.jsonl
done

# few-shot
DEVICE=0,1,2,3
splits=("test" "val")
model=""
model_dir=""
template="olympic_llama3_8b_instruct_icl"

for split in ${splits[@]}; do
  CUDA_VISIBLE_DEVICES=${DEVICE} python -u -m src.inference_olympic \
    --split ${split} \
    --prompt_type few-shot \
    --template ${template} \
    --stop "Question" "Answer" \
    --model ${model} \
    --model_dir ${model_dir} \
    --output_filename olympic_outputs/${model}/${split}/${template}/output.jsonl
done

# temperature sampling
DEVICE=0,1,2,3
split="test"
model=""
model_dir=""

for ((seed=0; seed<10; seed++)); do
  CUDA_VISIBLE_DEVICES=${DEVICE} python -u -m evaluation.olympic \
    --split ${split} \
    --seed ${seed} \
    --temperature 1.0 \
    --stop "Question" "Answer" \
    --model ${model} \
    --model_dir ${model_dir} \
    --output_filename olympic_outputs/${model}/${split}/t1.0/seed${seed}/output.jsonl
done