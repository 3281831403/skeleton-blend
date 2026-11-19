"""骨骼动画混合：四元数、遮罩与根运动的核心实现。"""


def normalize_weights(weights):
    """归一化混合权重，使总和为 1；总和为 0 时退化为均匀分布。"""
    weights = list(weights)
    total = sum(weights)
    if total == 0:
        if not weights:
            return []
        share = 1.0 / len(weights)
        return [share] * len(weights)
    return [w / total for w in weights]


def quaternion_dot_sign(a, b):
    """四元数点积为负时返回 -1，保证混合走最短弧。"""
    dot = sum(x * y for x, y in zip(a, b))
    return -1 if dot < 0 else 1


def clamp_additive(base, additive, limit):
    """加法层结果钳制到 ±limit。"""
    value = base + additive
    return max(-limit, min(limit, value))


def apply_bone_mask(weights, mask):
    """按骨骼遮罩过滤权重：被遮罩的骨骼置 0，其余重新归一化。"""
    masked = [w if m else 0.0 for w, m in zip(weights, mask)]
    total = sum(masked)
    if total == 0:
        return masked
    return [w / total for w in masked]


def extract_root_motion(delta, root_weight):
    """根运动只按根骨骼权重提取一次。"""
    return [d * root_weight for d in delta]


def sync_time(local_time, remote_time, blend):
    """本地与远端时间按 blend 同步。"""
    return local_time + (remote_time - local_time) * blend


def ik_blend(current, target, weight):
    """IK 目标按权重平滑混合。"""
    return [c + (t - c) * weight for c, t in zip(current, target)]


def mirror_bone_index(index, count):
    """镜像骨骼索引映射。"""
    return count - 1 - index


def cache_key(skeleton_id, clip):
    """动画缓存按骨架与片段隔离。"""
    return f"{skeleton_id}:{clip}"


def commit_poses(statuses):
    """批量姿势全部成功才提交。"""
    return all(statuses)
