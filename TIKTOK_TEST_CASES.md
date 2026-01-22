# TikTok Video Upload - Test Cases

## Test Case 1
**Test Case ID:** TC_UPLOAD_001
**Title:** Valid_File_Format
**Requirement:** System must be in MP4, MOV, MPEG, AVI or WebM format
**Test Type:** Positive 
**Preconditions:** user has the correct file Content Policy, size, length, resolution, aspect ratio, Frame Rate, and caption and Hashtags(if applicable).
**Test Steps:**  
 - [ ] Tap "+" button to access upload screen
 - [ ] Tap "Upload" to select from device storage
 - [ ] Select test video file "test_video.mp4"
 - [ ] Verify video preview loads
 - [ ] Tap "Next"
 - [ ] Add caption: "Test upload"
 - [ ] Tap "Post"
**Test Data:** Format: MOV
**Expected Result:** File uploads correctly because the format is one of the correct type. The videos appears on the users profile and is playable.
**Priority:** High
##### format instanceof (MP4, MOV, MPEG, AVI, WebM)


## Test Case 2
**Test Case ID:** TC_UPLOAD_002
**Title:** Valid_File_Size
**Requirement:** file size must be 1mb <= byte <= 287mb
**Test Type:** Positive 
**Preconditions:** user has the correct file Content Policy, Format, length, resolution, aspect ratio, Frame Rate, and caption and Hashtags(if applicable).
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
**Expected Result:** File uploads correctly because the file is ate the correct size. The videos appears on the users profile and is playable.
**Priority:** Medium

## Test Case 3
**Test Case ID:** TC_UPLOAD_003
**Title:** Invalid_Video_Length_Range
**Requirement:** File length is 600 < length < 3
**Test Type:** Negative 
**Preconditions:** user has the correct file Content Policy, size, format, resolution, aspect ratio, Frame Rate, and caption and Hashtags(if applicable).
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
**Expected Result:** File uploads incorrectly because the file length is to long. The video is to long for TikTok.
**Priority:** Medium

## Test Case 4
**Test Case ID:** TC_UPLOAD_004
**Title:** Valid_Video_Resolution
**Requirement:** file resolution is 720X1280 <= res <= 1080x1920
**Test Type:** Boundary
**Preconditions:** user has the correct file Content Policy, size, length, format, aspect ratio, Frame Rate, and caption and Hashtags(if applicable).
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
**Title:** Valid_Video_Aspect_Ratio
**Requirement:** file Aspect_Ratio is 9:16
**Test Type:** Boundary
**Preconditions:** user has the correct file Content Policy, size, length, resolution, format, Frame Rate, and caption and Hashtags(if applicable).
**Test Steps:**  
 - [ ] film video
 - [ ] check file size
 - [ ] Tap "+" button to access upload screen
 - [ ] Tap "Upload" to select from device storage
 - [ ] Verify video preview loads
 - [ ] Tap "Next"
 - [ ] Add caption: "Test upload"
 - [ ] Tap "Post"
**Test Data:** File Aspect_Ratio: 9:16
**Expected Result:** File uploads correctly because the ratio is correct. The videos appears on the users profile and is playable.
**Priority:** High

## Test Case 6
**Test Case ID:** TC_UPLOAD_006
**Title:** Invalid_Caption_Characters
**Requirement:** file Caption characters <= 2200
**Test Type:** Negative
**Preconditions:** user has the correct file Content Policy, format, size, length, resolution, aspect ratio, Frame Rate, caption, and Hashtags(if applicable).
**Test Steps:**  
 - [ ] film video
 - [ ] check file size
 - [ ] Tap "+" button to access upload screen
 - [ ] Tap "Upload" to select from device storage
 - [ ] Verify video preview loads
 - [ ] Tap "Next"
 - [ ] Add caption
 - [ ] Tap "Post"
**Test Data:** File Caption characters: 6767
**Expected Result:** File uploads incorrectly because there are to many characters in the caption. The videos appears on the users profile and is playable.
**Priority:** low

## Test Case 7
**Test Case ID:** TC_UPLOAD_007
**Title:** Valid_Frame_Rate
**Requirement:** file Frame Rate is 30 > fps < 60
**Test Type:** Black Box
**Preconditions:** user has the correct file Content Policy, size, length, format, aspect ratio, Frame Rate, and caption and Hashtags(if applicable).
**Test Steps:**  
- [ ] film video
- [ ] check file size
- [ ] Tap "+" button to access upload screen
- [ ] Tap "Upload" to select from device storage
- [ ] Verify video preview loads
- [ ] Tap "Next"
- [ ] Add caption: "Test upload"
- [ ] Tap "Post"
**Test Data:** File Frame Rate: 40
**Expected Result:** File uploads correctly because the Frame Rate is in range. The videos appears on the users profile and is playable.
**Priority:** High

## Test Case 8
**Test Case ID:** TC_UPLOAD_008
**Title:** Valid_Amount_Of_Hashtags
**Requirement:** Amount of Hashtags <=30
**Test Type:** Edge case
**Preconditions:** user has the correct file Content Policy, size, length, format, aspect ratio, Frame Rate, and Hashtags and caption(if applicable).
**Test Steps:**  
 - [ ] film video
 - [ ] check file size
 - [ ] Tap "+" button to access upload screen
 - [ ] Tap "Upload" to select from device storage
 - [ ] Verify video preview loads
 - [ ] Tap "Next"
 - [ ] Add caption: "Test upload"
 - [ ] Tap "Post"
**Test Data:** Amount of Hashtags: 0
**Expected Result:** File uploads correctly because there is the correct amount of Hashtags per video but this video has to Hashtags. The videos appears on the users profile and is playable.
**Priority:** Low

## Test Case 9
**Test Case ID:** TC_UPLOAD_009
**Title:** Valid_Amount_Of_Characters_Per_Hashtags
**Requirement:** Amount of Character <=20
**Test Type:** Edge case
**Preconditions:** user has the correct file Content Policy, size, length, format, aspect ratio, Frame Rate, and Hashtags and caption(if applicable).
**Test Steps:**  
 - [ ] film video
 - [ ] check file size
 - [ ] Tap "+" button to access upload screen
 - [ ] Tap "Upload" to select from device storage
 - [ ] Verify video preview loads
 - [ ] Tap "Next"
 - [ ] Add caption: "Test upload"
 - [ ] Tap "Post"
**Test Data:** Amount of Character: Null
**Expected Result:** File uploads incorrectly because there is the no character in Hashtags.
**Priority:** Low

## Test Case 10
**Test Case ID:** TC_UPLOAD_010
**Title:** Appropriate_Content
**Requirement:** No content can be (violence, nudity, hate speech)
**Test Type:** Black Box
**Preconditions:** user has the correct file Content Policy, size, length, format, aspect ratio, Frame Rate, and caption and Hashtags(if applicable).
**Test Steps:**  
 film video
 check file size
 Tap "+" button to access upload screen
 Tap "Upload" to select from device storage
 Verify video preview loads
 Tap "Next"
 Add caption: "Test upload"
 Tap "Post"
**Test Data:** Content: Hate speech against our leader Kim Jong Biruk
**Expected Result:** File uploads incorrectly because the Hate speech against our leader Kim Jong Biruk.
**Priority:** Low