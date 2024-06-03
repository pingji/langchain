from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Tongyi

llm = Tongyi()
text = llm.invoke("请给我写一句情人节红玫瑰的中文宣传语")
print(text)