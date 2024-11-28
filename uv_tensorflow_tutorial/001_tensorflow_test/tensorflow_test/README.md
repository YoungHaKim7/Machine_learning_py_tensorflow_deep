# Result


```bash
$ uv run hello.py

Using CPython 3.12.3 interpreter at: /usr/bin/python3.12
Creating virtual environment at: .venv
Installed 49 packages in 114ms
2024-11-28 20:05:27.496311: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2024-11-28 20:05:27.504226: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1732791927.512322    6665 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1732791927.514710    6665 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2024-11-28 20:05:27.523226: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
Hello from tensorflow01!
/home/g/tensorflow_test/.venv/lib/python3.12/site-packages/keras/src/layers/convolutional/base_conv.py:107: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
I0000 00:00:1732791932.070665    6665 gpu_device.cc:2022] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 5748 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 3060 Ti, pci bus id: 0000:01:00.0, compute capability: 8.6
Epoch 1/10
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1732791932.831530    6752 service.cc:148] XLA service 0x7b1460009880 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
I0000 00:00:1732791932.831548    6752 service.cc:156]   StreamExecutor device (0): NVIDIA GeForce RTX 3060 Ti, Compute Capability 8.6
2024-11-28 20:05:32.841283: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:268] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.
I0000 00:00:1732791932.888171    6752 cuda_dnn.cc:529] Loaded cuDNN version 90501
I0000 00:00:1732791933.670498    6752 device_compiler.h:188] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.
1500/1500 - 3s - 2ms/step - accuracy: 0.9464 - loss: 0.1837 - val_accuracy: 0.9776 - val_loss: 0.0731
Epoch 2/10
1500/1500 - 1s - 832us/step - accuracy: 0.9812 - loss: 0.0621 - val_accuracy: 0.9791 - val_loss: 0.0667
Epoch 3/10
1500/1500 - 1s - 848us/step - accuracy: 0.9876 - loss: 0.0408 - val_accuracy: 0.9814 - val_loss: 0.0612
Epoch 4/10
1500/1500 - 1s - 900us/step - accuracy: 0.9903 - loss: 0.0310 - val_accuracy: 0.9858 - val_loss: 0.0519
Epoch 5/10
1500/1500 - 1s - 874us/step - accuracy: 0.9937 - loss: 0.0203 - val_accuracy: 0.9837 - val_loss: 0.0588
Epoch 6/10
1500/1500 - 1s - 835us/step - accuracy: 0.9950 - loss: 0.0155 - val_accuracy: 0.9833 - val_loss: 0.0591
Epoch 7/10
1500/1500 - 1s - 848us/step - accuracy: 0.9961 - loss: 0.0119 - val_accuracy: 0.9874 - val_loss: 0.0534
Epoch 8/10
1500/1500 - 1s - 854us/step - accuracy: 0.9972 - loss: 0.0101 - val_accuracy: 0.9847 - val_loss: 0.0575
Epoch 9/10
1500/1500 - 1s - 821us/step - accuracy: 0.9978 - loss: 0.0070 - val_accuracy: 0.9832 - val_loss: 0.0688
Epoch 10/10
1500/1500 - 1s - 854us/step - accuracy: 0.9977 - loss: 0.0074 - val_accuracy: 0.9854 - val_loss: 0.0631
313/313 ━━━━━━━━━━━━━━━━━━━━ 1s 1ms/step - accuracy: 0.9816 - loss: 0.0715    
Test accuracy: 0.98
/home/g/tensorflow_test/hello.py:51: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
  plt.show()

```
