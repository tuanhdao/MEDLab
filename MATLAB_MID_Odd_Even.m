%% Behaviroal File Converter for MID fMRI experiment
% MID: Two sessions, Trial Type: Incentive (1), Neutral (3)
% Feedback: Win (4), Neutral (5), Loss (6)

clear all; clc;
%% load data
cd='\\ces.it.vanderbilt.edu\kujawalab\data\CASA\fMRI\Behavioral\MID';
subj='CASA1002';
Sess1 = readtable([subj '_11_MID-3_fMRI_Output.txt']);
Sess2 = readtable([subj '_12_MID-3_fMRI_Output.txt']);
%% time adjustment
% to synchronize with fMRI data acquisition time, 
% experiment (the first cue onset) should start at 2 sec
% Sess 1
Cue_Onset1 = Sess1.Cue_Onset(1);
FB_Onset1 = Sess1.FB_Onset(1);
Adjust1=Cue_Onset1-2000;
Sess1.Adj_CueOnset=(Sess1.Cue_Onset-Adjust1)/1000; % subtract and convert to sec
Sess1.Adj_FBOnset=(Sess1.FB_Onset-Adjust1)/1000;
Sess1.Ant_duration=Sess1.Ant_duration/1000; %convert to sec
% Sess 2
Cue_Onset2 = Sess2.Cue_Onset(1);
FB_Onset2 = Sess2.FB_Onset(2);
Adjust2=Cue_Onset2-2000; 
Sess2.Adj_CueOnset=(Sess2.Cue_Onset-Adjust2)/1000;
Sess2.Adj_FBOnset=(Sess2.FB_Onset-Adjust2)/1000;
Sess2.Ant_duration=Sess2.Ant_duration/1000;

%% incentive behavioral file
% Sess 1
Incen_Onset=Sess1.Adj_CueOnset(ismember(Sess1.Trial_Type,1))';
Incen_Onset_Odd=Incen_Onset(1:2:end);
Incen_Onset_Even=Incen_Onset(2:2:end);
Neut_Onset=Sess1.Adj_CueOnset(ismember(Sess1.Trial_Type,3))';
Neut_Onset_Odd=Neut_Onset(1:2:end);
Neut_Onset_Even=Neut_Onset(2:2:end);
Incen_Dur=Sess1.Ant_duration(ismember(Sess1.Trial_Type,1))';
Incen_Dur_Odd=Incen_Dur(1:2:end);
Incen_Dur_Even=Incen_Dur(2:2:end);
Neut_Dur=Sess1.Ant_duration(ismember(Sess1.Trial_Type,3))';
Neut_Dur_Odd=Neut_Dur(1:2:end);
Neut_Dur_Even=Neut_Dur(2:2:end);

names{1}='incentive_odd';
names{2}= 'incentive_even'; 
names{3}='neut_odd';
names{4}='neut_even';
onsets{1}=Incen_Onset_Odd;
onsets{2}=Incen_Onset_Even;
onsets{3}=Neut_Onset_Odd;
onsets{4}=Neut_Onset_Even;
durations{1}=Incen_Dur_Odd;
durations{2}=Incen_Dur_Even;
durations{3}=Neut_Dur_Odd;
durations{4}=Neut_Dur_Even;

save([subj '_run1_MID_incentive.mat'],'names', 'onsets', 'durations');

% Sess 2
Incen_Onset=Sess2.Adj_CueOnset(ismember(Sess2.Trial_Type,1))';
Incen_Onset_Odd=Incen_Onset(1:2:end);
Incen_Onset_Even=Incen_Onset(2:2:end);
Neut_Onset=Sess2.Adj_CueOnset(ismember(Sess2.Trial_Type,3))';
Neut_Onset_Odd=Neut_Onset(1:2:end);
Neut_Onset_Even=Neut_Onset(2:2:end);
Incen_Dur=Sess2.Ant_duration(ismember(Sess2.Trial_Type,1))';
Incen_Dur_Odd=Incen_Dur(1:2:end);
Incen_Dur_Even=Incen_Dur(2:2:end);
Neut_Dur=Sess2.Ant_duration(ismember(Sess2.Trial_Type,3))';
Neut_Dur_Odd=Neut_Dur(1:2:end);
Neut_Dur_Even=Neut_Dur(2:2:end);

names{1}='incentive_odd';
names{2}= 'incentive_even'; 
names{3}='neut_odd';
names{4}='neut_even';
onsets{1}=Incen_Onset_Odd;
onsets{2}=Incen_Onset_Even;
onsets{3}=Neut_Onset_Odd;
onsets{4}=Neut_Onset_Even;
durations{1}=Incen_Dur_Odd;
durations{2}=Incent_Dur_Even;
durations{3}=Neut_Dur_Odd;
durations{4}=Neut_Dur_Even;

save([subj '_run2_MID_incentive.mat'],'names', 'onsets', 'durations');

%% feedback behavioral file
% Sess 1
Win_Onset=Sess1.Adj_FBOnset(ismember(Sess1.Feedback,4))';
Win_Onset_Odd=Win_Onset(1:2:end);
Win_Onset_Even=Win_Onset(2:2:end);
Neut_Onset=Sess1.Adj_FBOnset(ismember(Sess1.Feedback,5))';
Neut_Onset_Odd=Neut_Onset(1:2:end);
Neut_Onset_Even=Neut_Onset(2:2:end);
Loss_Onset=Sess1.Adj_FBOnset(ismember(Sess1.Feedback,6))';
Loss_Onset_Odd=Loss_Onset(1:2:end);
Loss_Onset_Even=Loss_Onset(2:2:end);

names{1}='win_odd';
names{2}='win_even';
names{3}='neut_odd';
names{4}='neut_even';
names{5}='loss_odd';
names{6}='loss_even';
onsets{1}=Win_Onset_Odd;
onsets{2}=Win_Onset_Even;
onsets{3}=Neut_Onset_Odd; 
onsets{4}=Neut_Onset_Even;
onsets{5}=Loss_Onset_Odd;
onsets{6}=Loss_Onset_Even;
durations{1}=2;
durations{2}=2;
durations{3}=2;

save([subj '_run1_MID_feedback.mat'],'names', 'onsets', 'durations');

% Sess 2
Win_Onset=Sess2.Adj_FBOnset(ismember(Sess2.Feedback,4))';
Win_Onset_Odd=Win_Onset(1:2:end);
Win_Onset_Even=Win_Onset(2:2:end);
Neut_Onset=Sess2.Adj_FBOnset(ismember(Sess2.Feedback,5))';
Neut_Onset_Odd=Neut_Onset(1:2:end);
Neut_Onset_Even=Neut_Onset(2:2:end);
Loss_Onset=Sess2.Adj_FBOnset(ismember(Sess2.Feedback,6))';
Loss_Onset_Odd=Loss_Onset(1:2:end);
Loss_Onset_Even=Loss_Onset(2:2:end);

names{1}='win_odd';
names{2}='win_even';
names{3}='neut_odd';
names{4}='neut_even';
names{5}='loss_odd';
names{6}='loss_even';
onsets{1}=Win_Onset_Odd;
onsets{2}=Win_Onset_Even;
onsets{3}=Neut_Onset_Odd; 
onsets{4}=Neut_Onset_Even;
onsets{5}=Loss_Onset_Odd;
onsets{6}=Loss_Onset_Even;
durations{1}=2;
durations{2}=2;
durations{3}=2;
durations{4}=2;
durations{5}=2;
durations{6}=2;


save([subj '_run2_MID_feedback.mat'],'names', 'onsets', 'durations');
