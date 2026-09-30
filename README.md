# CG 生图与 Seedance 视频 Prompt Compiler

同一个 [SKILL.md](SKILL.md) 覆盖两条工作流：

- **CG 静态生图与改图**：适配用户指定的 Image 2.5、Image 2.0、Nano Banana Pro。按目标图锁定、参考图职责、唯一修改区域、结构、材质、光影和针对性限制编译可复制提示词。
- **Seedance 视频**：适配 2.0 和 2.5。未指定视频模型时默认 2.5；按剧情分段、镜头、素材绑定、对白、空间连续性和段界编译 Generation Unit。
- **先资产后视频**：先生成或精修角色、场景、道具图片，确认身份和材质后再绑定到 Seedance 的分镜与视频提示词。

## 使用示例

| 请求 | 输出 |
| --- | --- |
| “用 Image 2.5 优化图一的金属材质，图二只参考纹理” | 锁定图一结构与颜色、明确图二职责的完整改图提示词 |
| “把这张图做成精细白模，背景纯白，后景也清晰” | 保留原结构与细节的白模提示词 |
| “给我 Nano Banana Pro 精简版，只改头发，脸不要变” | 自然语言局部编辑提示词，不使用数值权重 |
| “用 Seedance 做这段剧情的分镜和可复制提示词” | 默认 2.5 的分段与视频提示词 |
| “按 Seedance 2.0 编译同一场戏” | 按 2.0 能力与单次时长重新拆分 |
| “两种 Image 模型分别写一版，再接 Seedance 2.5” | 各自独立的生图提示词与资产绑定后的视频提示词 |

图片模型遵从用户本次明确选择，未指定时继承当前项目最近使用的模型；无记录时暂按 Image 2.5 编译。只写“2.5”时根据当前是静态图片还是视频任务解释为 Image 2.5 或 Seedance 2.5。这里的 Image 2.0/2.5 是用户使用的模型名称，技能不假设其平台 API 参数。

## CG 生图规则

- 图一、图二等素材各有明确职责，材质参考图不覆盖目标图造型、颜色、构图和镜头。
- 只锁当前任务真正需要保持的属性；需要换视角、改结构或换色时，不写与目标冲突的“全部不变”。
- 材质用纹理方向和尺度、粗糙度、倒角、反射、厚度、受光与遮挡等可见证据描述。禁止以锐化和噪点代替细节。
- 白模、正侧背三视图、角色脸与头发、服装织物、金属木材、植物土壤和风格海报按各自结构与材质规则处理。
- Image 2.5 复杂任务可用分段完整指令，并防噪点与纹理中断；Image 2.0 保留核心锁定与改动；Nano Banana Pro 使用自然语言局部编辑并严防颜色漂移。这些是项目经验，不是未经证实的模型硬参数。

## Seedance 版本边界

| 模型 | 单次生成时长 | 参考素材上限 |
| --- | --- | --- |
| Seedance 2.0 | 官方模型报告为 4–15 秒，具体档位看平台 | 9 图、3 视频、3 音频 |
| Seedance 2.5 | 最长 30 秒，具体档位看平台 | 30 图、10 视频、10 音频 |

2.0 的时长和素材数量见 [官方模型论文](https://arxiv.org/abs/2604.14148)，2.5 见 [ByteDance Seed 官方发布说明](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)。Nano Banana Pro 的自然语言提示词组织参考 [Google 官方指南](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/)。具体界面功能以用户所用平台为准。

## 文件

- [SKILL.md](SKILL.md)：现行完整技能，包含 CG 生图与 Seedance 双版本视频规则。
- [agents/openai.yaml](agents/openai.yaml)、[assets/icon.svg](assets/icon.svg)：技能展示信息和图标。
- [Seedance-2-Prompt-Compiler-Standalone.md](Seedance-2-Prompt-Compiler-Standalone.md)、[references/](references/) 和 [scripts/](scripts/)：先前的 2.0 版本资料，保留供查阅；现行技能以根目录 SKILL.md 为准。

桌面端若通过下载三个文件进行本地安装，修改仓库不会自动改写电脑上的副本；更新时重新下载 SKILL.md 和 agents/openai.yaml 即可。
