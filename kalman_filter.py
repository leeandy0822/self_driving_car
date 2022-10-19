import numpy as np
from numpy.linalg import inv

class KalmanFilter():
    def __init__(self, x=0, y=0, yaw=0):
        # State [x, y, yaw]
        self.x = np.array([x, y, yaw])
        # Transition matrix
        self.A = np.identity(3)
        self.B = np.identity(3)
        # Error matrix
        self.P = np.identity(3) * 1
        # Observation matrix
        self.H = np.array([[1, 0, 0],
                           [0, 1, 0]])
        # State transition error covariance
        self.Q = np.identity(3) * 0.0002
        # Measurement error
        self.R = np.identity(2) * 0.003

    def predict(self, u):
        self.x = self.A @ self.x + self.B @ u
        self.P = self.A @ self.P @ np.transpose(self.A) + self.Q
        print(self.A.shape)
        
    def update(self, z):
        print(self.H@self.P@np.transpose(self.H))
        
        kalman_gain = self.P@np.transpose(self.H)@inv(self.H@self.P@np.transpose(self.H) + self.R)
        self.x = self.x + kalman_gain@(z - self.H@self.x)
        self.P = (np.identity(3) - kalman_gain@self.H)@self.P
        return self.x, self.P
