#include "Common.h"
#include <cstdarg>
#include <vector>

// ========================================================
// TSMaster 入口文件：负责 DLL 管理与函数注册
// ========================================================

TTSApp app; 
TTSCOM com; 
TTSTest test;

native_int report_handle = -1;
s32 diag_module_index = -1;
#define TEMP_STR_LEN 1024


// Utility functions definition
void internal_log(const char* AFile, const char* AFunc, const s32 ALine, const TLogLevel ALevel, const char* fmt, ...)
{ 
  va_list ap;    
  va_start(ap, fmt);
  std::vector<char> buf(1024);
  int ret;  
#if __cplusplus == 201103L
  while((ret = vsnprintf_s(&buf[0], buf.size(), fmt, ap)) == -1){
#else
  // in VC++ version is 199711L, log("__cplusplus: %d\n", __cplusplus);
  while ((ret = vsnprintf_s(&buf[0], buf.size(), buf.size(), fmt, ap)) == -1) {
#endif
    buf.resize(buf.size() * 2);    
  }
  va_end(ap);
  if (ret == static_cast<int>(buf.size())){
    buf[buf.size() - 1] = '\0';    
  }         
  app.debug_log(AFile, AFunc, ALine, &buf[0], ALevel);
}

void internal_test_log(const char* AFile, const char* AFunc, const s32 ALine, const TLogLevel ALevel, const char* fmt, ...)
{ 
  va_list ap;    
  va_start(ap, fmt);
  std::vector<char> buf(1024);
  int ret;  
#if __cplusplus == 201103L
  while ((ret = vsnprintf_s(&buf[0], buf.size(), fmt, ap)) == -1) {
#else
  while ((ret = vsnprintf_s(&buf[0], buf.size(), buf.size(), fmt, ap)) == -1) {
#endif
    buf.resize(buf.size() * 2);    
  }
  va_end(ap);
  if (ret == static_cast<int>(buf.size())){
    buf[buf.size() - 1] = '\0';    
  }         
  test.debug_log_info(AFile, AFunc, ALine, &buf[0], ALevel);
}

void test_logCAN(const char* ADesc, PCAN ACAN, const TLogLevel ALevel)
{
    char s[TEMP_STR_LEN];
    // channel, id, dlc, [data]
    if (ACAN->is_tx){
        if (ACAN->is_data){
            sprintf(s, "%s %d %03X Tx d %d [%02X %02X %02X %02X %02X %02X %02X %02X]", ADesc, ACAN->FIdxChn, ACAN->FIdentifier, ACAN->FDLC, ACAN->FData[0], ACAN->FData[1], ACAN->FData[2], ACAN->FData[3], ACAN->FData[4], ACAN->FData[5], ACAN->FData[6], ACAN->FData[7]);
        } else {
            sprintf(s, "%s %d %03X Tx r %d", ADesc, ACAN->FIdxChn, ACAN->FIdentifier, ACAN->FDLC);
        }
    } else {
        if (ACAN->is_data){
            sprintf(s, "%s %d %03X Rx d %d [%02X %02X %02X %02X %02X %02X %02X %02X]", ADesc, ACAN->FIdxChn, ACAN->FIdentifier, ACAN->FDLC, ACAN->FData[0], ACAN->FData[1], ACAN->FData[2], ACAN->FData[3], ACAN->FData[4], ACAN->FData[5], ACAN->FData[6], ACAN->FData[7]);
        } else {
            sprintf(s, "%s %d %03X Rx r %d", ADesc, ACAN->FIdxChn, ACAN->FIdentifier, ACAN->FDLC);
        }
    }
    test.log_info(s, ALevel);
}

// 在此处定义can发送/接收，变量变化等各种TSMaster的回调函数
TMPTimerMSUpg1 NewTimer1;
TMPTimerMsGroup NewTimer_Group1;
// 启动事件 "NewOn_Start1"
void on_start_NewOn_Start1(void) { try { // 程序启动事件
    app.log_text("on_start_NewOn_Start1",lvlInfo);

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// CAN报文接收事件 "NewOn_CAN_Rx1" 针对标识符  = 任意
void on_can_rx_NewOn_CAN_Rx1(const TCAN* ACAN) { try {  // 针对标识符  = 任意
// if (ACAN->FIdxChn != CH1) return; // if you want to filter channel
    app.log_text("on_can_rx_NewOn_CAN_Rx1",lvlInfo);
} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// CAN报文接收事件 "NewOn_CAN_FD_Rx1" 针对标识符  = 任意 (FD)
void on_canfd_rx_NewOn_CAN_FD_Rx1(const TCANFD* ACANFD) { try {  // 针对标识符  = 任意 (FD)
// if (ACANFD->FIdxChn != CH1) return; // if you want to filter channel

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// CAN报文发送成功事件 "NewOn_CAN_Tx1" 针对标识符  = 任意
void on_can_tx_NewOn_CAN_Tx1(const TCAN* ACAN) { try {  // 针对标识符  = 任意
// if (ACAN->FIdxChn != CH1) return; // if you want to filter channel

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// CAN报文发送成功事件 "NewOn_CAN_FD_Tx1" 针对标识符  = 任意 (FD)
void on_canfd_tx_NewOn_CAN_FD_Tx1(const TCANFD* ACANFD) { try {  // 针对标识符  = 任意 (FD)
// if (ACANFD->FIdxChn != CH1) return; // if you want to filter channel

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}
// CODE BLOCK END On_CAN_FD_Tx NewOn_CAN_FD_Tx1


// CAN报文预发送事件 "NewOn_CAN_PreTx1" 针对标识符  = 任意
void on_can_pretx_NewOn_CAN_PreTx1(const PCAN ACAN) { try {  // 针对标识符  = 任意
// if (ACAN->FIdxChn != CH1) return; // if you want to filter channel

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// CAN报文预发送事件 "NewOn_CAN_FD_PreTx1" 针对标识符  = 任意 (FD)
void on_canfd_pretx_NewOn_CAN_FD_PreTx1(const PCANFD ACANFD) { try {  // 针对标识符  = 任意 (FD)
// if (ACANFD->FIdxChn != CH1) return; // if you want to filter channel

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// LIN报文接收事件 "NewOn_LIN_Rx1" 针对标识符  = 任意
void on_lin_rx_NewOn_LIN_Rx1(const TLIN* ALIN) { try {  // 针对标识符  = 任意
// if (ALIN->FIdxChn != CH1) return; // if you want to filter channel

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// LIN报文发送成功事件 "NewOn_LIN_Tx1" 针对标识符  = 任意
void on_lin_tx_NewOn_LIN_Tx1(const TLIN* ALIN) { try {  // 针对标识符  = 任意
// if (ALIN->FIdxChn != CH1) return; // if you want to filter channel

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// LIN报文预发送事件 "NewOn_LIN_PreTx1" 针对标识符  = 任意
void on_lin_pretx_NewOn_LIN_PreTx1(const PLIN ALIN) { try {  // 针对标识符  = 任意
// if (ALIN->FIdxChn != CH1) return; // if you want to filter channel

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// 变量变化事件 "NewOn_Var_Change1" 针对变量 "未关联变量" [On Written]
void on_var_change_NewOn_Var_Change1(void) { try { // 变量 = 未关联变量

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// 定时器触发事件 "NewOn_Timer1" for Timer NewTimer1
void on_timer_NewOn_Timer1(void) { try { // 定时器 = NewTimer1

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// 定时器组触发事件 "NewOn_Timer_Group1" for Timer Group NewTimer_Group1
void on_timer_group_NewOn_Timer_Group1(const s32 AIndex) { try { // 定时器组 = NewTimer_Group1

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// 停止事件 "NewOn_Stop1"
void on_stop_NewOn_Stop1(void) { try { // 程序停止事件

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// 按键事件 "NewOn_Shortcut1" 快捷键 = Ctrl+R
void on_shortcut_NewOn_Shortcut1(const s32 AShortcut) { try { // 按键事件 = Ctrl+R

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}

// 主step函数，执行周期 5 ms
void step(void) { try { // 周期 = 5 ms

} catch (...) { log_nok("CRASH detected"); app.terminate_application(); }}



// 在此处声明 test_suites.cpp 中的具体测试函数
extern s32 Demo_TestCase_TerminalResistor(void);
extern s32 test_1001(void);

extern s32 test_report_init();
extern s32 test_final();

extern "C" {
    // 库初始化
    __declspec(dllexport) s32 __stdcall initialize_miniprogram(const PTSMasterConfiguration AConf) {
        app = AConf->FTSApp; 
        com = AConf->FTSCOM; 
        test = AConf->FTSTest;
        return 0;
    }

    // 库卸载
    __declspec(dllexport) s32 __stdcall finalize_miniprogram(void) { 
        return 0; 
    }
    
    // TSMaster 函数注册回调类型定义
    typedef s32 (__stdcall* TRegTSMasterFunction)(const void* AObj, const char* AFuncType, const char* AFuncName, const char* AData, const void* AFuncPointer, const char* ADescription);
    
    // 导出能力注册函数
    __declspec(dllexport) s32 __stdcall retrieve_mp_abilities(const void* AObj, const TRegTSMasterFunction AReg) {
        // --- 注册自定义测试用例 ---
        AReg(AObj, "on_custom_callback", "test_report_init", "", (const void*)&test_report_init, "");
        AReg(AObj, "on_custom_callback", "test_final", "", (const void*)&test_final, "");
        // AReg(AObj, "on_custom_callback", "TestReportInit", "", (const void*)&TestReportInit, "");
        // AReg(AObj, "on_custom_callback", "TestFinal", "", (const void*)&TestFinal, "");
        AReg(AObj, "on_custom_callback", "Demo_TestCase_TerminalResistor", "", (const void*)&Demo_TestCase_TerminalResistor, "");
        AReg(AObj, "on_custom_callback", "test_1001", "", (const void*)&test_1001, "");
        
        #define TSMASTER_VERSION "2026.4.16.1939"
        if (!AReg(AObj, "check_mp_internal", "version", TSMASTER_VERSION, 0, "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_app", (void *)sizeof(TTSMasterConfiguration), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_tcan", (void *)sizeof(TCAN), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_tcanfd", (void *)sizeof(TCANFD), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_tlin", (void *)sizeof(TLIN), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_tflexray", (void *)sizeof(TFlexRay), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_tethernetheader", (void *)sizeof(TEthernetHeader), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_TMPVarInt", (void *)sizeof(TMPVarInt), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_TMPVarDouble", (void *)sizeof(TMPVarDouble), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_TMPVarString", (void *)sizeof(TMPVarString), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_TMPVarCAN", (void *)sizeof(TMPVarCAN), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_TMPVarCANFD", (void *)sizeof(TMPVarCANFD), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_TMPVarLIN", (void *)sizeof(TMPVarLIN), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_TLIBTSMapping", (void *)sizeof(TLIBTSMapping), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "struct_size", "struct_size_TLIBSystemVarDef", (void *)sizeof(TLIBSystemVarDef), "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "auto_start", "0", 0, "")) return -1;
        if (!AReg(AObj, "check_mp_internal", "addr_conf", "app", &app, "")) return -1;

        if (!AReg(AObj, "step_function", "step", "5", reinterpret_cast<const void*>(&step), "")) return -1;
        if (!AReg(AObj, "timer_upg1", "NewTimer1", "100", reinterpret_cast<const void*>(&NewTimer1), "")) return -1;
        if (!AReg(AObj, "timer_group", "NewTimer_Group1", "100,3", reinterpret_cast<const void*>(&NewTimer_Group1), "")) return -1;
        if (!AReg(AObj, "on_can_rx_callback", "on_can_rx_NewOn_CAN_Rx1", "-1,-1,0", reinterpret_cast<const void*>(&on_can_rx_NewOn_CAN_Rx1), "")) return -1;
        if (!AReg(AObj, "on_can_rx_callback", "on_canfd_rx_NewOn_CAN_FD_Rx1", "-1,-1,-1", reinterpret_cast<const void*>(&on_canfd_rx_NewOn_CAN_FD_Rx1), "")) return -1;
        if (!AReg(AObj, "on_can_tx_callback", "on_can_tx_NewOn_CAN_Tx1", "-1,-1,0", reinterpret_cast<const void*>(&on_can_tx_NewOn_CAN_Tx1), "")) return -1;
        if (!AReg(AObj, "on_can_tx_callback", "on_canfd_tx_NewOn_CAN_FD_Tx1", "-1,-1,-1", reinterpret_cast<const void*>(&on_canfd_tx_NewOn_CAN_FD_Tx1), "")) return -1;
        if (!AReg(AObj, "on_can_pretx_callback", "on_can_pretx_NewOn_CAN_PreTx1", "-1,-1,0", reinterpret_cast<const void*>(&on_can_pretx_NewOn_CAN_PreTx1), "")) return -1;
        if (!AReg(AObj, "on_can_pretx_callback", "on_canfd_pretx_NewOn_CAN_FD_PreTx1", "-1,-1,-1", reinterpret_cast<const void*>(&on_canfd_pretx_NewOn_CAN_FD_PreTx1), "")) return -1;
        if (!AReg(AObj, "on_lin_rx_callback", "on_lin_rx_NewOn_LIN_Rx1", "-1", reinterpret_cast<const void*>(&on_lin_rx_NewOn_LIN_Rx1), "")) return -1;
        if (!AReg(AObj, "on_lin_tx_callback", "on_lin_tx_NewOn_LIN_Tx1", "18", reinterpret_cast<const void*>(&on_lin_tx_NewOn_LIN_Tx1), "")) return -1;
        if (!AReg(AObj, "on_lin_pretx_callback", "on_lin_pretx_NewOn_LIN_PreTx1", "-1", reinterpret_cast<const void*>(&on_lin_pretx_NewOn_LIN_PreTx1), "")) return -1;
        if (!AReg(AObj, "on_var_change_callback", "on_var_change_NewOn_Var_Change1", "未关联变量", reinterpret_cast<const void*>(&on_var_change_NewOn_Var_Change1), "")) return -1;
        if (!AReg(AObj, "on_timer_callback", "on_timer_NewOn_Timer1", "NewTimer1", reinterpret_cast<const void*>(&on_timer_NewOn_Timer1), "")) return -1;
        if (!AReg(AObj, "on_timer_group_callback", "on_timer_group_NewOn_Timer_Group1", "NewTimer_Group1", reinterpret_cast<const void*>(&on_timer_group_NewOn_Timer_Group1), "")) return -1;
        if (!AReg(AObj, "on_start_callback", "on_start_NewOn_Start1", "", reinterpret_cast<const void*>(&on_start_NewOn_Start1), "")) return -1;
        if (!AReg(AObj, "on_stop_callback", "on_stop_NewOn_Stop1", "", reinterpret_cast<const void*>(&on_stop_NewOn_Stop1), "")) return -1;
        if (!AReg(AObj, "on_shortcut_callback", "on_shortcut_NewOn_Shortcut1", "Ctrl+R", reinterpret_cast<const void*>(&on_shortcut_NewOn_Shortcut1), "")) return -1;

        // MP library functions
        // MP Library test_report
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_init", "const pnative_int Handle", &test_report.test_init, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_set_report_name", "const native_int Handle, const char* reportName", &test_report.test_set_report_name, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_title", "const native_int Handle,const char* testgroup, const char* testcase, const char* image, const char* testpurpose", &test_report.test_title, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_step", "const native_int Handle,const char* step,const char* AMsg", &test_report.test_step, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_pass", "const native_int Handle,const char* step,const char* AMsg", &test_report.test_pass, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_fail", "const native_int Handle,const char* step,const char* AMsg", &test_report.test_fail, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_warning", "const native_int Handle,const char* step,const char* AMsg", &test_report.test_warning, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_na", "const native_int Handle,const char* step,const char* AMsg", &test_report.test_na, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_final", "const native_int Handle", &test_report.test_final, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_openissue", "const native_int Handle,const char* openissueinfo", &test_report.test_openissue, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_testinfo", "const native_int Handle, const char* ProductName, const char* HWVersion, const char* SWVersion,const char* DUTVersion, const char* TestEngineer, const char* ManufacturerName", &test_report.test_testinfo, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_set_watermark", "const native_int Handle,const char* AWaterMark", &test_report.test_set_watermark, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_set_html_name_and_logo", "const native_int Handle,const char* AHtmlName,const char* ALogoName", &test_report.test_set_html_name_and_logo, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.test_export", "const char* csvfilePath, const char* HtmlFilePath", &test_report.test_export, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "test_report.sddb_to_json", "const char* sddbfile, const char* jsonfile", &test_report.sddb_to_json, "0")) return -1;
        // MP Library rtlUIDiagnostics
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_create", "ps32 pDiagModuleIndex, u32 AChnIndex, u8 ASupportFDCAN, u8 AMaxDLC,u32 ARequestID, bool ARequestIDIsStd, u32 AResponseID, bool AResponseIDIsStd, u32 AFunctionID, bool AFunctionIDIsStd", &rtlUIDiagnostics.tsdiag_can_create, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_delete", "s32 ADiagModuleIndex", &rtlUIDiagnostics.tsdiag_can_delete, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_delete_all", "", &rtlUIDiagnostics.tsdiag_can_delete_all, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_delete", "s32 ADiagModuleIndex", &rtlUIDiagnostics.tsdiag_delete, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_delete_all", "", &rtlUIDiagnostics.tsdiag_delete_all, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_set_p2_timeout", "s32 ADiagModuleIndex, s32 ATimeMs", &rtlUIDiagnostics.tsdiag_set_p2_timeout, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_set_p2_extended", "s32 ADiagModuleIndex, s32 ATimeMs", &rtlUIDiagnostics.tsdiag_set_p2_extended, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_set_s3_servertime", "s32 ADiagModuleIndex, s32 ATimeMs", &rtlUIDiagnostics.tsdiag_set_s3_servertime, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_set_s3_clienttime", "s32 ADiagModuleIndex, s32 ATimeMs", &rtlUIDiagnostics.tsdiag_set_s3_clienttime, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_set_filled_byte", "s32 ADiagModuleIndex, u8 AFilledByte", &rtlUIDiagnostics.tsdiag_set_filled_byte, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_set_at_least_8bytes", "s32 ADiagModuleIndex, s32 AIs8Bytes", &rtlUIDiagnostics.tsdiag_set_at_least_8bytes, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_set_fcdelay", "s32 ADiagModuleIndex, s32 AFCDelay", &rtlUIDiagnostics.tsdiag_set_fcdelay, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_send_functional", "s32 ADiagModuleIndex, pu8 AReqDataArray, s32 AReqDataSize", &rtlUIDiagnostics.tstp_send_functional, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_send_request", "s32 ADiagModuleIndex, pu8 AReqDataArray, s32 AReqDataSize", &rtlUIDiagnostics.tstp_send_request, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_request_and_get_response", "s32 ADiagModuleIndex, pu8 AReqDataArray, s32 AReqDataSize, pu8 AResponseDataArray, ps32 AResponseDataSize", &rtlUIDiagnostics.tstp_request_and_get_response, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_request_and_get_response_functional", "s32 ADiagModuleIndex, pu8 AReqDataArray, s32 AReqDataSize, pu8 AResponseDataArray, ps32 AResponseDataSize", &rtlUIDiagnostics.tstp_request_and_get_response_functional, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_can_send_functional", "s32 ADiagModuleIndex, pu8 AReqDataArray, s32 AReqDataSize", &rtlUIDiagnostics.tstp_can_send_functional, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_can_send_request", "s32 ADiagModuleIndex, pu8 AReqDataArray, s32 AReqDataSize", &rtlUIDiagnostics.tstp_can_send_request, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_can_request_and_get_response", "s32 ADiagModuleIndex, pu8 AReqDataArray, s32 AReqDataSize, pu8 AResponseDataArray, ps32 AResponseDataSize", &rtlUIDiagnostics.tstp_can_request_and_get_response, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_can_request_and_get_response_functional", "s32 ADiagModuleIndex, pu8 AReqDataArray, s32 AReqDataSize, pu8 AResponseDataArray, ps32 AResponseDataSize", &rtlUIDiagnostics.tstp_can_request_and_get_response_functional, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_session_control", "s32 ADiagModuleIndex, u8 ASubSession", &rtlUIDiagnostics.tsdiag_session_control, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_communication_control", "s32 ADiagModuleIndex, u8 AControlType", &rtlUIDiagnostics.tsdiag_communication_control, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_routine_control", "s32 ADiagModuleIndex, u8 ARoutineControlType, u16 ARoutintID", &rtlUIDiagnostics.tsdiag_routine_control, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_security_access_request_seed", "s32 ADiagModuleIndex, s32 ALevel, pu8 ARecSeed, ps32 ARecSeedSize", &rtlUIDiagnostics.tsdiag_security_access_request_seed, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_security_access_send_key", "s32 ADiagModuleIndex, s32 ALevel, pu8 AKeyValue, s32 AKeySize", &rtlUIDiagnostics.tsdiag_security_access_send_key, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_request_download", "s32 ADiagModuleIndex, u32 AMemAddr, u32 AMemSize", &rtlUIDiagnostics.tsdiag_request_download, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_request_upload", "s32 ADiagModuleIndex, u32 AMemAddr, u32 AMemSize", &rtlUIDiagnostics.tsdiag_request_upload, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_transfer_data", "s32 ADiagModuleIndex, pu8 ASourceData, s32 ADataSize, s32 AReqCase", &rtlUIDiagnostics.tsdiag_transfer_data, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_request_transfer_exit", "s32 ADiagModuleIndex", &rtlUIDiagnostics.tsdiag_request_transfer_exit, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_write_data_by_identifier", "s32 ADiagModuleIndex, u16 ADataIdentifier, pu8 AWriteData, s32 AWriteDataSize", &rtlUIDiagnostics.tsdiag_write_data_by_identifier, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_read_data_by_identifier", "s32 ADiagModuleIndex, u16 ADataIdentifier, pu8 AReturnArray, ps32 AReturnArraySize", &rtlUIDiagnostics.tsdiag_read_data_by_identifier, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_session_control", "s32 ADiagModuleIndex, u8 ASubSession", &rtlUIDiagnostics.tsdiag_can_session_control, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_communication_control", "s32 ADiagModuleIndex, u8 AControlType", &rtlUIDiagnostics.tsdiag_can_communication_control, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_routine_control", "s32 ADiagModuleIndex, u8 ARoutineControlType, u16 ARoutintID", &rtlUIDiagnostics.tsdiag_can_routine_control, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_security_access_request_seed", "s32 ADiagModuleIndex, s32 ALevel, pu8 ARecSeed, ps32 ARecSeedSize", &rtlUIDiagnostics.tsdiag_can_security_access_request_seed, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_security_access_send_key", "s32 ADiagModuleIndex, s32 ALevel, pu8 AKeyValue, s32 AKeySize", &rtlUIDiagnostics.tsdiag_can_security_access_send_key, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_request_download", "s32 ADiagModuleIndex, u32 AMemAddr, u32 AMemSize", &rtlUIDiagnostics.tsdiag_can_request_download, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_request_upload", "s32 ADiagModuleIndex, u32 AMemAddr, u32 AMemSize", &rtlUIDiagnostics.tsdiag_can_request_upload, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_transfer_data", "s32 ADiagModuleIndex, pu8 ASourceData, s32 ADataSize, s32 AReqCase", &rtlUIDiagnostics.tsdiag_can_transfer_data, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_request_transfer_exit", "s32 ADiagModuleIndex", &rtlUIDiagnostics.tsdiag_can_request_transfer_exit, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_write_data_by_identifier", "s32 ADiagModuleIndex, u16 ADataIdentifier, pu8 AWriteData, s32 AWriteDataSize", &rtlUIDiagnostics.tsdiag_can_write_data_by_identifier, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_can_read_data_by_identifier", "s32 ADiagModuleIndex, u16 ADataIdentifier, pu8 AReturnArray, ps32 AReturnArraySize", &rtlUIDiagnostics.tsdiag_can_read_data_by_identifier, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_set_is_valid", "s32 ADiagModuleIndex, bool AIsValid", &rtlUIDiagnostics.tsdiag_set_is_valid, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_set_fdmode", "s32 ADiagModuleIndex, bool AFDMode, bool ASupportBRS, s32 AMaxDLC", &rtlUIDiagnostics.tsdiag_set_fdmode, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_lin_create", "ps32 pDiagModuleIndex, u32 AChnIndex, u8 ANad", &rtlUIDiagnostics.tsdiag_lin_create, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_lin_set_run_with_normal_schedule_table", "s32 ADiagModuleIndex, bool ADiagRunWithNormalScheduleTable", &rtlUIDiagnostics.tstp_lin_set_run_with_normal_schedule_table, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_lin_tp_para_default", "s32 ADiagModuleIndex, u16 AReqIntervalMs, u16 AResIntervalMs, u16 AResRetryTime", &rtlUIDiagnostics.tstp_lin_tp_para_default, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tstp_lin_tp_para_special", "s32 ADiagModuleIndex, u16 AReqIntervalMs, u16 AResIntervalMs, u16 AResRetryTime", &rtlUIDiagnostics.tstp_lin_tp_para_special, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_lin_set_nad", "s32 ADiagModuleIndex, u8 ANAD", &rtlUIDiagnostics.tsdiag_lin_set_nad, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_doip_create", "ps32 pDiagModuleIndex, s32 AToolType, u32 AChnIndex, char* ATesterIP, u16 ATesterPort, char* ADUTIP, u16 ADUTPort, u32 ARequestID, u32 AResponseID, u32 AFunctionID", &rtlUIDiagnostics.tsdiag_doip_create, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_doip_set_version", "s32 ADiagModuleIndex, s32 AVersion", &rtlUIDiagnostics.tsdiag_doip_set_version, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_doip_connect", "s32 ADiagModuleIndex", &rtlUIDiagnostics.tsdiag_doip_connect, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_doip_routing_activation", "s32 ADiagModuleIndex, u8 AActivateType, bool ASendOEMSpecificData, u32 AOEMSpecificData", &rtlUIDiagnostics.tsdiag_doip_routing_activation, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_doip_disconnect", "s32 ADiagModuleIndex", &rtlUIDiagnostics.tsdiag_doip_disconnect, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_ui_get_handle_by_name", "char* AModuleName, ps32 APDiagModuleIndex", &rtlUIDiagnostics.tsdiag_ui_get_handle_by_name, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_ui_load_db", "s32 ADiagModuleIndex, char* ADBPath", &rtlUIDiagnostics.tsdiag_ui_load_db, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_ui_get_service_list", "s32 ADiagModuleIndex, s32 AServiceID, char** AServiceList", &rtlUIDiagnostics.tsdiag_ui_get_service_list, "0")) return -1;
        if (!AReg(AObj, "reg_mp_library_func", "rtlUIDiagnostics.tsdiag_ui_execute_service", "s32 ADiagModuleIndex, s32 AServiceID, char* AServiceName, char* AParameters, char** AResult", &rtlUIDiagnostics.tsdiag_ui_execute_service, "0")) return -1;
        return 1;
    }
}
