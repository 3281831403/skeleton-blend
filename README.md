# 骨骼动画混合：四元数、遮罩与根运动

角色在跑步和挥手之间切换时关节翻转：四元数混合走了长弧，权重和超过 1，加法层没有钳制，骨骼遮罩没生效，根运动被重复提取，本地与远端时间不同步，IK 混合突变，镜像骨骼索引错位，缓存按片段名共享，批量姿势只提交一半。

## 目录结构

```
README.md
conftest.py
.gitignore
animation/__init__.py
animation/skeleton_blend.py
tests/test_skeleton_blend.py
```

## 当前状态

`animation/skeleton_blend.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_skeleton_blend.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 四元数按最短弧混合
2. 混合权重归一化
3. 加法层按上限钳制
4. 骨骼遮罩生效
5. 根运动只提取一次
6. 本地与远端时间同步
7. IK 权重平滑混合
8. 镜像骨骼索引映射
9. 缓存按骨架隔离
10. 批量姿势统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `animation/skeleton_blend.py`
后 15 条用例应全部通过。
