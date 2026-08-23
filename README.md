# Seedance 2.0 Prompt Compiler

把剧本、分镜、对话剧、解说漫、3D 国漫、游戏 CG 等内容编译为 **Seedance 2.0 可执行**的剧情分段、Generation Unit、镜头方案与视频提示词。

## 核心能力

- **剧情分段**：按叙事节点拆分视频段落，做时长预算，不固定段长、不强迫切镜
- **分镜设计**：镜头表达、站位、切镜与空间连续性，按情绪选择虫视 / POV / 俯拍 / 仰拍等镜头
- **高级运镜**：希区柯克变焦、英雄环绕、甩镜、长镜头等技法，按叙事节点调用
- **段界衔接**：独立生成单元的尾镜—首镜配对与跳帧规避，保证人物 / 场景资产跨段连续
- **提示词输出**：生成可直接投喂 Seedance 2.0 的视频提示词与 Generation Unit

## 使用场景

| 输入 | 输出 |
|---|---|
| 剧本 / 小说文本 | 剧情分段 + 分镜 + 视频提示词 |
| 已有分镜表 | 优化后的镜头方案 + 提示词 |
| 人物 / 场景 / 道具参考 | 多模态资产引用与衔接方案 |
| 上一段成片 | 续写提示词（继承结束状态） |

## 目录结构

```
├── SKILL.md                                  # 技能定义与工作流
├── Seedance-2-Prompt-Compiler-Standalone.md  # 独立完整版编译器
├── references/                               # 参考规范
│   ├── segmentation.md            # 剧情分段与时长预算
│   ├── segment-boundaries.md      # 段界配对与跳帧规避
│   ├── shot-language.md           # 镜头语言与连续性
│   ├── emotion-shot-library.md    # 情绪镜头库
│   ├── advanced-camera-moves.md   # 高级运镜技法
│   └── prompt-output.md           # 提示词输出格式
├── scripts/
│   └── build_standalone.py       # 独立版构建脚本
├── agents/
│   └── openai.yaml               # Agent 配置
└── assets/
    └── icon.svg                  # 图标
```

## 设计原则

- 剧情忠实 > 生成便利
- 连续性 > 局部炫技
- 真实表演容量 > 固定段长
- 情绪变化驱动镜头变化 > 平视中景铺满全场
- 不默认视频比例，不因模型上限删剧情、删台词
