import transformers

model = transformers.BertForQuestionAnswering.from_pretrained("bert-base-uncased")

question = "What is the capital of France?"

answer = model.predict(question)

print(answer)