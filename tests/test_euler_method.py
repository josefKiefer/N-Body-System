import pytest
from unittest.mock import patch
from src.models import VectorizedBody
from src.euler_method import euler
import numpy as np

def test_euler_zero_acceleration_bodies_dont_move():
  with patch("src.euler_method.get_accelerations") as mock_get_accelerations:
    body1 = VectorizedBody("Body1", 
                           1,
                           np.array([0.0, 0.0]),
                           np.array([0.0, 0.0]))
    body2 = VectorizedBody("Body2",
                            1,
                           np.array([0.0, 0.0]),
                           np.array([0.0, 0.0]))

    mock_get_accelerations.return_value = (np.array([0.0, 0.0]), np.array([0.0, 0.0]))

    body1_pos, body2_pos = euler(1, 3, body1, body2)

    assert len(body1_pos) == 3
    assert len(body2_pos) == 3
    assert body1_pos[0].shape == (2,)
    mock_get_accelerations.assert_called_with(body1, body2)
    assert mock_get_accelerations.call_count == 3
    assert all(np.array_equal(p, np.array([0.0, 0.0])) for p in body1_pos)
    assert all(np.array_equal(p, np.array([0.0, 0.0])) for p in body2_pos)

def test_euler_constant_acceleration_bodies_move():
  with patch("src.euler_method.get_accelerations") as mock_get_accelerations:
    body1 = VectorizedBody("Body1", 
                           1,
                           np.array([0.0, 0.0]),
                           np.array([0.0, 0.0]))
    body2 = VectorizedBody("Body2",
                            1,
                           np.array([0.0, 0.0]),
                           np.array([0.0, 0.0]))

    mock_get_accelerations.return_value = (np.array([1.0, 0.0]), np.array([0.0, 1.0]))

    body1_pos, body2_pos = euler(1, 3, body1, body2)

    assert len(body1_pos) == 3
    assert len(body2_pos) == 3
    mock_get_accelerations.assert_called_with(body1, body2)

    assert body1_pos[0][0] == np.float64(0.0)
    assert body1_pos[0][1] == np.float64(0.0)
    assert body1_pos[1][0] == np.float64(1.0)
    assert body1_pos[1][1] == np.float64(0.0)
    assert body1_pos[2][0] == np.float64(3.0)
    assert body1_pos[2][1] == np.float64(0.0)
    
    assert body2_pos[0][0] == np.float64(0.0)
    assert body2_pos[0][1] == np.float64(0.0)
    assert body2_pos[1][0] == np.float64(0.0)
    assert body2_pos[1][1] == np.float64(1.0)
    assert body2_pos[2][0] == np.float64(0.0)
    assert body2_pos[2][1] == np.float64(3.0)

def test_euler_num_steps_ceil():
  with patch("src.euler_method.get_accelerations") as mock_get_accelerations:
    body1 = VectorizedBody("Body1", 
                           1,
                           np.array([0.0, 0.0]),
                           np.array([0.0, 0.0]))
    body2 = VectorizedBody("Body2",
                            1,
                           np.array([0.0, 0.0]),
                           np.array([0.0, 0.0]))

    mock_get_accelerations.return_value = (np.array([0.0, 0.0]), np.array([0.0, 0.0]))

    body1_pos, body2_pos = euler(0.3, 1, body1, body2)

    assert len(body1_pos) == 4
    assert len(body2_pos) == 4
    mock_get_accelerations.assert_called_with(body1, body2)
    assert mock_get_accelerations.call_count == 4

def test_euler_num_steps_single():
  with patch("src.euler_method.get_accelerations") as mock_get_accelerations:
    body1 = VectorizedBody("Body1", 
                           1,
                           np.array([0.0, 0.0]),
                           np.array([0.0, 0.0]))
    body2 = VectorizedBody("Body2",
                            1,
                           np.array([0.0, 0.0]),
                           np.array([0.0, 0.0]))
    
    mock_get_accelerations.return_value = (np.array([0.0, 0.0]), np.array([0.0, 0.0]))
    
    body1_pos, body2_pos = euler(1, 1, body1, body2)

    assert len(body1_pos) == 1
    assert len(body2_pos) == 1
    mock_get_accelerations.assert_called_with(body1, body2)
    assert mock_get_accelerations.call_count == 1

def test_euler_pure_velocity_drift():
  with patch("src.euler_method.get_accelerations") as mock_get_accelerations:
    body1 = VectorizedBody("Body1", 
                           1,
                           np.array([0.0, 0.0]),
                           np.array([1.0, 1.0]))
    body2 = VectorizedBody("Body2",
                            1,
                           np.array([0.0, 0.0]),
                           np.array([1.0, 1.0]))

    mock_get_accelerations.return_value = (np.array([0.0, 0.0]), np.array([0.0, 0.0]))

    body1_pos, body2_pos = euler(1, 3, body1, body2)

    assert len(body1_pos) == 3
    assert len(body2_pos) == 3
    mock_get_accelerations.assert_called_with(body1, body2)

    assert body1_pos[0][0] == np.float64(0.0)
    assert body1_pos[0][1] == np.float64(0.0)
    assert body1_pos[1][0] == np.float64(1.0)
    assert body1_pos[1][1] == np.float64(1.0)
    assert body1_pos[2][0] == np.float64(2.0)
    assert body1_pos[2][1] == np.float64(2.0)
    
    assert body2_pos[0][0] == np.float64(0.0)
    assert body2_pos[0][1] == np.float64(0.0)
    assert body2_pos[1][0] == np.float64(1.0)
    assert body2_pos[1][1] == np.float64(1.0)
    assert body2_pos[2][0] == np.float64(2.0)
    assert body2_pos[2][1] == np.float64(2.0)