/*
  test_vc2017.cpp

  cam - gray - shift/drift Hue - alpha

OpenCV 3.4.12 https://github.com/opencv/opencv/releases/tag/3.4.12
OpenCV 4.5.0 https://github.com/opencv/opencv/releases/tag/4.5.0
とりあえず 3.4.12 で試す
 opencv-3.4.12-vc14_vc15.exe 実行(展開先 opencv-3.4.12-vc14_vc15 999MB)
  の中から build の中身のみ(827MB)を C:\OpenCV3 へ
 C:\OpenCV3\x64\vc15\bin の opencv_world3412.dll opencv_ffmpeg3412_64.dll
  (ffmpeg は C:\OpenCV3\bin の中に*も*ある) を ./ へ

(VC2017 の solution-project/MSBuild を使う場合は
 ..\x64\Release\test_vc2017_prj.exe 以外にもいくつか出来る
 - オプションで調整必要)

x64 のコンパイラを使用する
"C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\bin\Hostx64\x64\cl.exe"
 -source-charset:utf-8 -execution-charset:utf-8
 -EHsc -Fe..\x64\Release\test_vc2017_prj.exe test_vc2017.cpp
 -IC:\OpenCV3\include
  (-I"C:\Program Files (x86)\Windows Kits\10\Include\10.0.17763.0\ucrt")
  (-I"C:\Program Files (x86)\Windows Kits\10\Include\10.0.17763.0\um")
  (-I"C:\Program Files (x86)\Windows Kits\10\Include\10.0.17763.0\winrt")
  (-I"C:\Program Files (x86)\Windows Kits\10\Include\10.0.17763.0\shared")
 -link
  /LIBPATH:C:\OpenCV3\x64\vc15\lib
  /LIBPATH:"C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\lib\x64"
  /LIBPATH:"C:\Program Files (x86)\Windows Kits\10\Lib\10.0.17763.0\ucrt\x64"
  /LIBPATH:"C:\Program Files (x86)\Windows Kits\10\Lib\10.0.17763.0\um\x64"
  /LIBPATH:"C:\Program Files (x86)\Windows Kits\10\Lib\10.0.17763.0\winrt\x64"
   opencv_world3412.lib kernel32.lib user32.lib
del test_vc2017.obj
*/

#include "test_vc2017.h"

using namespace testVC2017;

bool MyWaitKey(int w)
{
#if 0
  struct timespec remain, req{0, w * 1000000}; // 0sec w * 1000000nsec
  nanosleep(&req, &remain);
#else
  ::Sleep(w); // ms
#endif
  MSG msg;
  while(::PeekMessage(&msg, NULL, 0, 0, PM_NOREMOVE)){
    int result = (int)::GetMessage(&msg, NULL, 0, 0);
    if(!result){ // WM_QUIT
      ::PostQuitMessage(msg.wParam);
      return false;
    }else if(result < 0){
      return true; // error occured
    }else{
      if(msg.message == WM_KEYDOWN && msg.wParam == VK_ESCAPE){
        return false;
      }
      ::TranslateMessage(&msg);
      ::DispatchMessage(&msg);
    }
  }
  return true;
}

cv::Mat mkGammaLUT(double g)
{
  cv::Mat lut(1, 256, CV_8U);
  uchar *p = lut.data;
  for(int i = 0; i < lut.cols; ++i)
    p[i] = cv::saturate_cast<uchar>(255.0 * pow(i / 255.0, g));
  return lut;
}

cv::Mat mkRotGammaLUT(double g)
{
  cv::Mat lut(1, 256, CV_8U);
  uchar *p = lut.data;
  for(int i = 0; i < lut.cols; ++i)
    p[i] = 255 - cv::saturate_cast<uchar>(255.0 * pow((255 - i) / 255.0, g));
  return lut;
}

string drift(int ac, char **av)
{
  // cv::InitSystem(ac, av);
  // cv::Mat gammaLUT = mkGammaLUT(2.2); // (1 / 2.2);
  cv::Mat gammaLUT = mkRotGammaLUT(2.2); // (1 / 2.2);
  vector<string> wn({"original", "gray", "Hue", "Alpha"});
  for(vector<string>::iterator i = wn.begin(); i != wn.end(); ++i)
    cv::namedWindow(*i, CV_WINDOW_AUTOSIZE | CV_WINDOW_FREERATIO);
  int cam_id = 1; // 0; // may be 'ManyCam Virtual Webcam'
  int width = 640, height = 480, fourcc;
  double fps = 30.0;
#if 0
  cv::VideoCapture cap;
  cap.open("http://.../...avi");
#else
  cv::VideoCapture cap(cv::CAP_DSHOW + cam_id); // use DirectShow
#endif
  if(!cap.isOpened()) return "error: open camera";
  // cout << cv::getBuildInformation() << endl;
  cout << "width: " << (int)cap.get(cv::CAP_PROP_FRAME_WIDTH) << endl;
  cout << "height: " << (int)cap.get(cv::CAP_PROP_FRAME_HEIGHT) << endl;
  cout << "fps: " << (double)cap.get(cv::CAP_PROP_FPS) << endl; // 0 ?
  if(!cap.set(cv::CAP_PROP_FRAME_WIDTH, width)) cout << "width err" << endl;
  if(!cap.set(cv::CAP_PROP_FRAME_HEIGHT, height)) cout << "height err" << endl;
  if(!cap.set(cv::CAP_PROP_FPS, fps)) cout << "fps err" << endl;
  cout << "fps: " << (double)cap.get(cv::CAP_PROP_FPS) << endl;
  // fourcc = cv::VideoWriter::fourcc('M', 'J', 'P', 'G');
  // fourcc = cv::VideoWriter::fourcc('m', 'p', '4', 'v');
  // fourcc = cv::VideoWriter::fourcc('X', 'V', 'I', 'D');
  // fourcc = cv::VideoWriter::fourcc('D', 'I', 'V', 'X');
  // fourcc = cv::VideoWriter::fourcc('X', '2', '6', '4');
  fourcc = 0x00000020; // fallback tag
  bool col = true;
  cv::VideoWriter wr(TEST_OUT, fourcc, fps, cv::Size(width, height), col);
  int cnt = 0;
  cv::Mat frm;
  while(true){
#if 0
    cap >> frm;
    if(frm.empty()) break;
#else
    if(!cap.read(frm)) break;
#endif
    cv::imshow(wn[0], frm);
#if 0
#if 0
#if 0
    cv::flip(frm, frm, 1); // left <-> right
    vector<uchar> buf;
    vector<int> args({CV_IMWRITE_JPEG_QUALITY, 95}); // default 95
    cv::imencode(".jpg", frm, buf, args);
    cv::Mat im = cv::imdecode(cv::Mat(buf), CV_LOAD_IMAGE_COLOR);
#else
    vector<uchar> buf;
    vector<int> args({CV_IMWRITE_PNG_COMPRESSION, 9}); // default 3 max 9
    cv::imencode(".png", frm, buf, args);
    cv::Mat im = cv::imdecode(cv::Mat(buf), CV_LOAD_IMAGE_COLOR);
#endif
#else
#if 0 // no compress fast
    vector<uchar> buf;
    vector<int> args({CV_IMWRITE_PXM_BINARY, 1}); // default 1
    cv::imencode(".ppm", frm, buf, args); // PPM (PGM PBM) must be .ppm only
    cv::Mat im = cv::imdecode(cv::Mat(buf), CV_LOAD_IMAGE_COLOR); // 0 gray
#else
    cv::Mat im;
    cv::cvtColor(frm, im, CV_BGR2GRAY);
    cv::GaussianBlur(im, im, cv::Size(7, 7), 1.5, 1.5); // blur
    cv::Canny(im, im, 0, 30, 3); // edge
#endif
#endif
#else
    cv::Mat gr, hsv;
    cv::cvtColor(frm, gr, CV_BGR2GRAY);
    cv::GaussianBlur(gr, gr, cv::Size(7, 7), 1.5, 1.5);
    cv::LUT(gr, gammaLUT, gr);
    cv::cvtColor(gr, gr, CV_GRAY2BGR);
    cv::imshow(wn[1], gr);
    vector<cv::Mat> pl; // B G R planes
    cv::split(gr, pl);
#if 0
    cv::MatIterator_<uchar> bi = pl[0].begin<uchar>(), be = pl[0].end<uchar>();
    for(; bi != be; ++bi) *bi = cv::saturate_cast<uchar>(32);
    cv::MatIterator_<uchar> gi = pl[1].begin<uchar>(), ge = pl[1].end<uchar>();
    for(; gi != ge; ++gi) *gi = cv::saturate_cast<uchar>(192);
    cv::MatIterator_<uchar> ri = pl[2].begin<uchar>(), re = pl[2].end<uchar>();
    for(; ri != re; ++ri) *ri = cv::saturate_cast<uchar>(240);
#else
    for(int j = 0; j < gr.rows; ++j){
      uchar *b = pl[0].ptr<uchar>(j);
      uchar *g = pl[1].ptr<uchar>(j);
      uchar *r = pl[2].ptr<uchar>(j);
      for(int i = 0; i < gr.cols; ++i){
        // uchar &pixel = pl[...].at<uchar>(j, i);
        // pixel = cv::saturate_cast<uchar>(...);
        // * may be more accurate with gamma processing before hue rotation *
        //uchar s = 0, e = 255, hue = 179 * b[i] / 255; // 0-255 -> 0-179
        //uchar s = 76, e = 255, hue = b[i] - 76; // 76-255 -> 0-179
        //uchar s = 166, e = 255, hue = 2 * (b[i] - 166); // 166-255 -> 0-179
        uchar s = 165, e = 254, hue = 2 * (b[i] - 165); // 165-254 -> 0-179
        //uchar s = 135, e = 224, hue = 2 * (b[i] - 135); // 135-224 -> 0-179
        //uchar s = 211, e = 255, hue = 4 * (b[i] - 211); // 211-255 -> 0-179
        //uchar s = 180, e = 224, hue = 4 * (b[i] - 180); // 180-224 -> 0-179
        //uchar s = 210, e = 254, hue = 4 * (b[i] - 210); // 210-254 -> 0-179
        //uchar s = 232, e = 254, hue = 8 * (b[i] - 232); // 232-254 -> 0-179
        bool f = (b[i] >= s) && (b[i] <= e);
        b[i] = cv::saturate_cast<uchar>((cnt + 179 - hue) % 180); // H
        g[i] = cv::saturate_cast<uchar>(f ? 255 : 0); // S
        r[i] = cv::saturate_cast<uchar>(255 - b[i]); // V
      }
    }
#endif
    cv::merge(pl, hsv);
    cv::cvtColor(hsv, hsv, CV_HSV2BGR); // assume BGR as HSV
    cv::imshow(wn[2], hsv); // hsv.channels() == 3
#if 0
    cv::Mat alpha = cv::imread(ALPHA_IN, cv::IMREAD_UNCHANGED); // channels: 4
    cv::Mat im(alpha.rows, alpha.cols, alpha.type());
#if 0
    im = cv::Scalar::all(128); // im = alpha;
#else
    vector<cv::Mat> pa; // B G R A planes
    cv::split(alpha, pa);
#if 0
    cv::split(hsv, pl);
    pa[0] = pl[0];
    pa[1] = pl[1];
    pa[2] = pl[2];
    // pa[3] = pa[3];
    cv::merge(pa, im);
#else
    hsv.copyTo(im, pa[3]);
#endif
#endif
    cv::imwrite(ALPHA_OUT, im); // default {CV_IMWRITE_PNG_COMPRESSION, 3}
#else
#if 0
    cv::Mat im(gr.rows, gr.cols, CV_8UC4);
    vector<cv::Mat> pa; // B G R A planes
    cv::split(im, pa);
    cv::split(hsv, pl);
    pa[0] = pl[0];
    pa[1] = pl[1];
    pa[2] = pl[2];
    pa[3] = 255;
    cv::merge(pa, im);
#else
    cv::Mat im(frm);
    hsv.copyTo(im, pl[1]);
    cv::addWeighted(frm, 0.5, im, 0.5, 0.0, im);
#endif
#endif
#endif
    wr << im;
    cv::imshow(wn[3], im);
    ++cnt;
#if 0
    int k = cv::waitKey(1); // 1ms > 15ms ! on Windows
    if(k == 'q' || k == '\x1b'){ cv::imwrite(IMG_OUT, im); break; }
#else
    if(!MyWaitKey(1) || cnt > 1000){ cv::imwrite(IMG_OUT, im); break; }
#endif
  }
#if 1 // any release functions will be called from destructor ?
  wr.release();
  cap.release();
  cv::destroyAllWindows();
#endif
  return "ok";
}

int main(int ac, char **av)
{
#if 0
  int a, b;
  cin >> a >> b;
  cout << a + b << endl;
#endif
  fprintf(stdout, "sizeof(size_t): %zd\n", sizeof(size_t));
  cout << drift(ac, av) << endl;
  fprintf(stdout, "done\n");
  return 0;
}
