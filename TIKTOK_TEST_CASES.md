# TikTok Video Upload - Test Cases

## Test Case 1
**Test Case ID:** TC_UPLOAD_001
**Title:** Valid_File_Format_Partition
**Requirement:** System must be in MP4, MOV, MPEG, AVI or WebM format
**Test Type:** Positive 
**Preconditions:** user has the correct file name, size, length, resolution, aspect ratio and caption(if applicable).
**Test Steps:**  
- [ ] Tap "+" button to access upload screen
- [ ] Tap "Upload" to select from device storage
- [ ] Select test video file "test_video.mp4"
- [ ] Verify video preview loads
- [ ] Tap "Next"
- [ ] Add caption: "Test upload"
- [ ] Tap "Post"
**Test Data:** Format: MOV
**Expected Result:** File uploads correctly. The videos appears on the users profile and is playable.
**Priority:** High
##### format instanceof (MP4, MOV, MPEG, AVI, WebM)


## Test Case 2
**Test Case ID:** TC_UPLOAD_002
**Title:** Valid_File_Size_Partitions
**Requirement:** file size must be 1mb <= byte <= 287mb
**Test Type:** Positive 
**Preconditions:** user has the correct file format, size, length, resolution, aspect ratio and caption(option).
**Test Steps:**  
- [ ] film video
- [ ] check file size
- [ ] Tap "+" button to access upload screen
- [ ] Tap "Upload" to select from device storage
- [ ] Verify video preview loads
- [ ] Tap "Next"
- [ ] Add caption: "Test upload"
- [ ] Tap "Post"
**Test Data:** File size: 2mb
**Expected Result:** File uploads correctly. The videos appears on the users profile and is playable.
**Priority:** Medium

## Test Case 3
**Test Case ID:** TC_UPLOAD_003
**Title:** Invalid_Video_Length_Range_Partitions
**Requirement:** File length is 600 < length < 3
**Test Type:** Negative 
**Preconditions:** user has the correct file format, size, type, resolution, aspect ratio and caption(option).
**Test Steps:**  
- [ ] film video
- [ ] don't check file length
- [ ] Tap "+" button to access upload screen
- [ ] Tap "Upload" to select from device storage
- [ ] Verify video preview loads
- [ ] Tap "Next"
- [ ] Add caption: "Test upload"
- [ ] Tap "Post"
**Test Data:** File length: 605
**Expected Result:** File uploads incorrectly. The video is to long for TikTok.
**Priority:** Medium

## Test Case 4
**Test Case ID:** TC_UPLOAD_004
**Title:** Valid_Video_Resolution_Partitions
**Requirement:** file resolution is 720X1280 <= res <= 1080x1920
**Test Type:** Boundary
**Preconditions:** user has the correct file format, size, length, type, aspect ratio and caption(option).
**Test Steps:**  
- [ ] film video
- [ ] check file size
- [ ] Tap "+" button to access upload screen
- [ ] Tap "Upload" to select from device storage
- [ ] Verify video preview loads
- [ ] Tap "Next"
- [ ] Add caption: "Test upload"
- [ ] Tap "Post"
**Test Data:** File resolution: 720x1280
**Expected Result:** File uploads correctly because the resolution is in range. The videos appears on the users profile and is playable.
**Priority:** High

## Test Case 5
**Test Case ID:** TC_UPLOAD_005
**Title:** Valid_Video_Aspect_Ratio_Partitions
**Requirement:** file resolution is 720X1280 <= res <= 1080x1920
**Test Type:** Boundary
**Preconditions:** user has the correct file format, size, length, type, aspect ratio and caption(option).
**Test Steps:**  
- [ ] film video
- [ ] check file size
- [ ] Tap "+" button to access upload screen
- [ ] Tap "Upload" to select from device storage
- [ ] Verify video preview loads
- [ ] Tap "Next"
- [ ] Add caption: "Test upload"
- [ ] Tap "Post"
**Test Data:** File resolution: 720x1280
**Expected Result:** File uploads correctly because the resolution is in range. The videos appears on the users profile and is playable.
**Priority:** High

## Test Case 6
**Test Case ID:** TC_UPLOAD_006
**Title:** Valid_Aspect_Ratio_Partitions
**Requirement:** file Aspect Ratio = 9:16
**Test Type:** Boundary
**Preconditions:** user has the correct file format, size, length, type, resolution and caption(option).
**Test Steps:**  
- [ ] film video
- [ ] check file size
- [ ] Tap "+" button to access upload screen
- [ ] Tap "Upload" to select from device storage
- [ ] Verify video preview loads
- [ ] Tap "Next"
- [ ] Add caption: "Test upload"
- [ ] Tap "Post"
**Test Data:** File Aspect Ratio: 9:16
**Expected Result:** File uploads correctly because the Aspect Ratio is to correct vertical type. The videos appears on the users profile and is playable.
**Priority:** High

## Test Case 7
**Test Case ID:** TC_UPLOAD_007
**Title:** Valid_Frame_Rate_Partitions
**Requirement:** file Frame_Rate = 9:16
**Test Type:** Black Box
**Preconditions:** user has the correct file format, size, length, type, resolution and caption(option).
**Test Steps:**  
- [ ] film video
- [ ] check file size
- [ ] Tap "+" button to access upload screen
- [ ] Tap "Upload" to select from device storage
- [ ] Verify video preview loads
- [ ] Tap "Next"
- [ ] Add caption: "Test upload"
- [ ] Tap "Post"
**Test Data:** File Aspect Ratio: 9:16
**Expected Result:** File uploads correctly because the Aspect Ratio is to correct vertical type. The videos appears on the users profile and is playable.
**Priority:** High

## Test Case 8
**Test Case ID:** TC_UPLOAD_008
**Title:** Valid_Hashtags_Partitions
**Requirement:** file Hashtags = 9:16
**Test Type:** Black Box
**Preconditions:** user has the correct file format, size, length, type, resolution, Frame_Rate and caption(option).
**Test Steps:**  
- [ ] film video
- [ ] check file size
- [ ] Tap "+" button to access upload screen
- [ ] Tap "Upload" to select from device storage
- [ ] Verify video preview loads
- [ ] Tap "Next"
- [ ] Add caption: "Test upload"
- [ ] Tap "Post"
**Test Data:** File Aspect Ratio: 9:16
**Expected Result:** File uploads correctly because the Aspect Ratio is to correct vertical type. The videos appears on the users profile and is playable.
**Priority:** High

