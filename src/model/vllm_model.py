import torch
from vllm import LLM, SamplingParams


class VLLMModel():
    def __init__(self, args):
        self.args = args
        num_gpus = torch.cuda.device_count()
        print('num_gpus', num_gpus)
        another_args = {'max_num_batched_tokens': args.max_num_batched_tokens}

        self.llm = LLM(model=args.model_dir, tensor_parallel_size=num_gpus, seed=args.seed, **another_args, trust_remote_code=args.trust_remote_code)
        print(">>>>>> model loaded")

        self.sampling_params = SamplingParams(temperature=args.temperature, top_p=args.top_p,
                                              max_tokens=args.max_tokens,
                                              stop=args.stop, presence_penalty=args.presence_penalty,
                                              frequency_penalty=args.frequency_penalty,
                                              logprobs=args.logprobs,
                                              prompt_logprobs=args.prompt_logprobs)

    def generate(self, processed_prompts):
        outputs = self.llm.generate(processed_prompts, self.sampling_params)
        sorted_outputs = sorted(outputs, key=lambda output: int(output.request_id))
        print(">>>>>> generation done")
        return sorted_outputs
