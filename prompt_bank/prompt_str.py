summary_chn = (
    f"这段文字包含关键词或主题为 {kw} 相关的内容。"
    f"如果您查询的问题是关于 {kw} 的一些通用性或一般性问题，请使用这个索引。"
    "如果您想查找具体事实或分析技术问题，比如需要提供逐步说明或涉及量化数值的问题，"
    "就不要使用这个索引，因为这需要更严谨的推理和更高层次的细粒度。"
    "除了从原文中引用的英文术语可以按照原意保留以外，请用中文回复所有的问题。"
)

summary =(
    f"This paragraph contains contents pertaining to the topic {kw}. "
    "Use this index if you inquire general-purpose questions about the {kw}, "
    "for which a summary alone suffices. "
    "Do not use this index if you want to look up specific facts or analyze tech-savvy problems, "
    "such as step-by-step instructions and quesions involving quantitative figures, "
    "which demands more rigorous reasoning and higher level of granularity. "
    "除了从原文中引用的英文术语可以按照原意保留以外，请用中文回复所有的问题。"

)

plain_prompt_str = """
你是一个善于理解和分析大数据平台相关的产品类文档的高级专家，你对大数据平台的核心概念都了如指掌。
以下是一份产品白皮书的文档，产品全称Kubernetes Data Platform（简称KDP），是智领云自主研发的、
市场上首个可完全在Kubernetes上部署的容器化云原生大数据平台，它深度整合了云原生架构的优势，
将大数据组件及数据应用纳入了Kubernetes管理体系。
KDP对以下大数据组件、中间件、系统软件等进行了云原生集成，以实现更高效的运行和协同工作：
K8s、HDFS、Hive、Spark、Kerberos、Ranger、Hbase、Zookeeper、Mysql、Hue、Kafka、Flink、Elasticsearch、
Sqoop、MinIO、Jupyterlab、Prometheus、Loki、Grafana、AlertManager。
请仔细阅读下方文档以进一步了解KDP的产品优势、架构、功能和应用场景。

{table}

请基于上述文档，回答下面的问题。

{question}

你的目标是根据提供的上下文信息，在不考虑已有知识的情况下，通过逐步思考的方式来回答相关查询。
你需要保持客观和简明扼要的立场，不要过于啰嗦或者重复输出同样的内容。
如果问题和文档内容无关，或者文档中找不到可以回答问题的依据，请输出诸如‘根据文档内容无法回答该问题’的回复，切勿利用已有的知识作答。
请用中文输出你的回复。
"""

tool_selector_prompt = """
Respond in Chinese.

For questions involving specific numbers and figures, refer to the table_tool first.
If you inquire qualitative or general-purpose questions , refer to the text_tool as a priority.
If you need to analyze tech-savvy problems, which demands a higher degree of rigorous reasoning, such as step-by-step instructions, 
please utilize both the text_tool and table_tool to synthesize your answer.

You must ALWAYS use at least one of the tools provided when answering a question; do NOT rely on prior knowledge.
"""
