# Artificial Intelligence Markup Language (AIML)

AIML是基于XML的人工智能标记语言, 由Alicebot自由软件社区和Richard S. Wallace博士在1995-2000期间开发。 AIML用于创建或自定义Alicebot，使用起来非常容易，即使您不是程序员也可以轻松学习。迄今为止市场上最复杂的智能对话系统就是由AIML来构建的, 包括屡获殊荣的Mitsuku聊天机器人。Mitsuku被广泛认为是最好的人工智能对话系统。

## AIML标签

* <aiml> 定义AIML文档的开头和结尾。
* <category> 定义Alicebot知识库中的知识单元。
* <pattern> 定义模式以匹配用户可以输入到Alicebot的模式。
* <template> 定义Alicebot对用户输入的响应。
   
AIML文件范例：
```
<aiml version = "1.0.1" encoding = "UTF-8"?>
   <category>
      <pattern> Hi Alice </pattern>

      <template>
         Hello XXX!
      </template>

   </category>
</aiml>
```

## Refers

* https://pandorabots.com/docs/aiml-basics/
