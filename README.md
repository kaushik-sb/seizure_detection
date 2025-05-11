Seizure detection using Oscillatory Neural Networks

This project implements seizure detection using pipeline preprocessing of FASTA data of a ECG signal followed by prediction through an Oscillatory Convolutional Neural network to detect seizures. The trained model is saved as a .pkl file for faster throughput and prediction latency. 

Oscillatory Convolutional Neural networks use wave-like spatial kernels to predict using signal input instead of using static kernels that leave out oscillation information during prediction. This allows us to better capture relative temporal data of wave-like signals to implement a correlation between the predicted output and the wave information of the ECG signal. 

A sample of rat ECG data is provided for testing, with both seizure-free and seizure-filled ECG data files. Results are displayed along with ECG signal representation within a side-scroll temporal graph. Number of seizures along with seizure-period highlighting of the ECG signal illustration has been implemented
