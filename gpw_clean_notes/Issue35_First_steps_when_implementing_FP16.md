2018-04-22: [First steps when implementing FP16](https://gpuopen.com/first-steps-implementing-fp16/)

- available with AMD vega architecture
- pack two FP16 into FP32 register
- reduce ALU instructions count, reduce VGPR usage
- how to detect FP16 code generation in FXC disassembly and GCN ISA output
- discussion of pitfalls and common use-cases
- how to deal with FP16 constants
