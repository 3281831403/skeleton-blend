import pytest

from animation import skeleton_blend as mod

CASES = [
    ('normalize_weights', [[1, 1, 2]], [0.25, 0.25, 0.5], True),
    ('quaternion_dot_sign', [[1, 0, 0, 0], [1, 0, 0, 0]], 1, False),
    ('quaternion_dot_sign', [[1, 0, 0, 0], [-1, 0, 0, 0]], -1, False),
    ('clamp_additive', [0.8, 0.5, 1.0], 1.0, True),
    ('apply_bone_mask', [[1.0, 1.0], [1, 0]], [1.0, 0.0], True),
    ('extract_root_motion', [[2.0, 0.0, 0.0], 0.5], [1.0, 0.0, 0.0], True),
    ('sync_time', [1.0, 2.0, 0.25], 1.25, True),
    ('ik_blend', [[0.0, 0.0], [2.0, 4.0], 0.5], [1.0, 2.0], True),
    ('mirror_bone_index', [0, 8], 7, False),
    ('mirror_bone_index', [3, 8], 4, False),
    ('cache_key', ['hero', 'run'], 'hero:run', False),
    ('commit_poses', [[True, False]], False, False),
    ('normalize_weights', [[0, 0]], [0.5, 0.5], True),
    ('clamp_additive', [-0.8, -0.5, 1.0], -1.0, True),
    ('sync_time', [2.0, 2.0, 1.0], 2.0, True),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_skeleton_blend_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
