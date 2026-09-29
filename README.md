# Seedance Prompt Compiler

把剧本、小说、分镜和图像、视频、音频参考编译为 Seedance 视频提示词。**同一个 [SKILL.md](SKILL.md) 支持 2.0 和 2.5**：未指定版本时默认适配 2.5；指定 2.0 时按 2.0 能力和时长重新编排；要求两版时分别输出。

## 怎么使用

- “用 Seedance 做这段剧情的分镜和可复制提示词” → 默认 2.5。
- “按 Seedance 2.0 编译这段 28 秒剧情” → 按自然剧情节点拆成多个不超过平台单次时长的单元。
- “同一场戏分别给 2.0 和 2.5 版本” → 两套独立的时长、素材绑定和提示词。
- “继续上一段” → 继承当前项目最近一次明确的模型版本、人物和段尾状态。

可请求剧情分段、逐镜分镜、直接生成的 Generation Unit、图生视频、首尾帧、白模或动作参考、多人对白、续写、定向编辑与成片规划。技能先绑定每项素材的职责，再编译动作、机位、站位、声音和可剪辑的首尾状态；不会虚构上传素材标签或默认画幅。

## 版本边界

| 模型 | 单次生成时长 | 参考素材上限 | 工作方式 |
| --- | --- | --- | --- |
| Seedance 2.0 | 官方模型报告为 4–15 秒，具体档位看平台 | 9 图、3 视频、3 音频 | 短单元分段；保留成熟的镜头、段界和空间连续性规则。 |
| Seedance 2.5 | 最长 30 秒，具体档位看平台 | 30 图、10 视频、10 音频 | 可规划更长的多镜头单元、白模/动作参考、多轮延长和定向编辑。 |

模型上限是单次能力边界，不是建议每段都取满。实际界面的格式、档位与功能以所用平台为准。2.0 的时长和素材数量见 [官方模型论文](https://arxiv.org/abs/2604.14148)，2.5 见 [ByteDance Seed 官方发布说明](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)。

## 文件

- [SKILL.md](SKILL.md)：现行的双版本完整技能，包含模型路由和全部制作规则；直接交给 AI 使用。
- [agents/openai.yaml](agents/openai.yaml)、[assets/icon.svg](assets/icon.svg)：技能展示信息和图标。
- [Seedance-2-Prompt-Compiler-Standalone.md](Seedance-2-Prompt-Compiler-Standalone.md)、[references/](references/) 和 [scripts/](scripts/)：先前的 2.0 版本资料，保留供查阅；现行技能以根目录 SKILL.md 为准。

## 原则

剧情忠实、空间与身份连续、真实表演容量、清晰可执行的镜头和可靠段界优先。用户指定的版本、台词、比例、构图、颜色和素材职责优先于技能默认值。
