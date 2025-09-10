max = 9;
fs = 1000;
for i = 1:2:max
% dsp.SineWave(amp,freq,phase,Name,Value);
wave = dsp.SineWave(1/i, i*2*pi, 0, ...
’SamplesPerFrame’, 5000, ’SampleRate’, fs);
y = wave();
if i == 1
wavesum = y;
else
wavesum = wavesum + y;
end
scope(wavesum());
pause(.5);
% waitforbuttonpress;
end