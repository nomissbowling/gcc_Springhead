/*
  test_vc2017.h
*/

#ifndef __TEST_VC2017_H__
#define __TEST_VC2017_H__

#include <opencv2/opencv.hpp>

#include <iomanip>
#include <iostream>
#include <vector>

#include <windows.h>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#define BASE_DIR "E:\\virtual"
#define ALPHA_IN BASE_DIR"\\cv3_alpha_in.png"
#define ALPHA_OUT BASE_DIR"\\cv3_alpha_out.png"
#define IMG_OUT BASE_DIR"\\cv3_img.png"
//#define TEST_OUT BASE_DIR"\\cv3_out.avi" // ('M', 'J', 'P', 'G')
#define TEST_OUT BASE_DIR"\\cv3_out.mp4" // ('m', 'p', '4', 'v')

namespace testVC2017 {

using namespace std;

}

#endif // __TEST_VC2017_H__
