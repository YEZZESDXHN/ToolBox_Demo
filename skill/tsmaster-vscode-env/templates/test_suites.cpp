#include "Common.h"
#include <cstdarg>
#include <vector>


TrtlUIDiagnostics rtlUIDiagnostics;
Ttest_report test_report;

// ========================================================
// 测试逻辑文件：在此处编写简洁的测试用例
// ========================================================


// s32 test_init(){
//     try
//     {
//         /* code */
//         app.log_text("start test_init1",lvlInfo);
//         return test_report.test_init(&report_handle);
//     }
//     catch(...)
//     {
//         app.log_text("Unexpected error in test_init", lvlError);
//         return IDX_ERR_MP_CODE_CRASH;
//     }
// }

s32 test_report_init()
{
    s32 ret;
    s64 Handle;
    // char report_name[] = "report";
    // if (&report_handle != nullptr) {
    //     // *AHandle = (native_int)Handle; 
    // }
    ret = test_report.test_init(&report_handle);
    // ret = test_report.test_set_report_name(AHandle, (char*)report_name);
    return ret;
}

void TestStep(const char* test_step, const char* format, ...) {
    va_list args;
    va_start(args, format);
    
    // 1. 计算所需长度
    va_list args_copy;
    va_copy(args_copy, args);
    int size = vsnprintf(nullptr, 0, format, args_copy);
    va_end(args_copy);

    if (size >= 0) {
        std::vector<char> buffer(size + 1);
        vsnprintf(buffer.data(), buffer.size(), format, args);
        
        // 2. 确保 test_step 不为 null，如果是空字符串则转为 ""
        const char* step_name = (test_step && test_step[0] != '\0') ? test_step : "";
        
        // 3. 调用底层
        test_report.test_step(report_handle, (char*)step_name, buffer.data());
    }
    va_end(args);
}

// TestStepPass 和 TestStepFail 依此类推，只需改最后一行调用的函数名即可
void TestStepPass(const char* test_step, const char* format, ...) {
    va_list args;
    va_start(args, format);
    int size = vsnprintf(nullptr, 0, format, args);
    if (size >= 0) {
        std::vector<char> buffer(size + 1);
        va_start(args, format); // 重新初始化 args
        vsnprintf(buffer.data(), buffer.size(), format, args);
        test_report.test_pass(report_handle, (char*)test_step, buffer.data());
        test.set_verdict_ok("Testcase Pass");
    }
    va_end(args);
}

void TestStepFail(const char* test_step, const char* format, ...) {
    va_list args;
    va_start(args, format);
    int size = vsnprintf(nullptr, 0, format, args);
    if (size >= 0) {
        std::vector<char> buffer(size + 1);
        va_start(args, format);
        vsnprintf(buffer.data(), buffer.size(), format, args);
        test_report.test_fail(report_handle, (char*)test_step, buffer.data());
        test.set_verdict_nok("Testcase Failed");
    }
    va_end(args);
}

s32 TestTitle(const char *tg_name, const char *tc_name, const char *tc_image, const char *tc_objective)
{
    return test_report.test_title(report_handle, tg_name, tc_name, tc_image, tc_objective);
}
s32 test_final()
{
    return test_report.test_final(report_handle);
}



// s32 test_init(){
//     try
//     {
//         app.log_text("start test_init", lvlInfo);

//         // 🛠️ 核心排查：检查 test_report 对象的函数指针是否为空！
//         // 如果你的 Ttest_report 结构体里的成员叫 test_init，可以直接这样判断：
//         if (test_report.test_init == nullptr) {
//             app.log_text("【致命错误】: test_report.test_init 函数指针为 NULL！底层 DLL 接口未绑定成功！", lvlError);
//             return -1; // 优雅拦截，阻止崩溃
//         }

//         // 如果指针不为空，再安全调用
//         return test_report.test_init(&report_handle);
//     }
//     catch(...)
//     {
//         app.log_text("Unexpected error in test_init", lvlError);
//         return IDX_ERR_MP_CODE_CRASH;
//     }
// }

// s32 test_final(){
//     try
//     {
//         /* code */
//         app.log_text("start test_final",lvlInfo);
//         return test_report.test_final(report_handle);
//     }
//     catch(...)
//     {
//         app.log_text("Unexpected error in test_final", lvlError);
//         return IDX_ERR_MP_CODE_CRASH;
//     }
// }


// 示例用例：终端电阻测试
s32 Demo_TestCase_TerminalResistor(void) {
    try {
        TestTitle("诊断", "终端电阻测试", "", "");
        // 模拟测试步骤
        TestStep("Step 1: Measuring CAN_H/L Resistance...", "Measuring CAN_H/L Resistance...");
        app.wait(500, "Waiting for relay stability");
        
        double measuredResistance = 61.2; // 模拟从硬件读取的测量结果
        
        if (measuredResistance > 55.0 && measuredResistance < 65.0) {
            TestStepPass("Step 2: Resistance check PASSED", "Resistance check PASSED (60 Ohm target)");
        } else {
            TestStepFail("Step 2: Resistance check FAILED", "Resistance check FAILED (60 Ohm target)");
        }

        app.log_text("--- End: Demo_TestCase_TerminalResistor ---", lvlInfo);
        return IDX_ERR_OK;
    } catch (...) {
        app.log_text("Unexpected error in Demo_TestCase", lvlError);
        return IDX_ERR_MP_CODE_CRASH;
    }
}

s32 test_1001(){
    try
    {
        // test_report_init();
        TestTitle("诊断", "测试1001", "", "");
        /* code */
        int udsHandle = -1;
        app.log_text("start tsdiag_can_create",lvlInfo);
        TestStep("step:tsdiag_can_create","tsdiag_can_create");
        if (rtlUIDiagnostics.tsdiag_can_create == nullptr) {
            app.log_text("rtlUIDiagnostics.tsdiag_can_create 函数指针为 NULL！底层 DLL 接口未绑定成功！", lvlError);
            return -1; // 优雅拦截，阻止崩溃
        }
        s32 ret = rtlUIDiagnostics.tsdiag_can_create(&udsHandle,CH1, 0, 8, 0x772, 1, 0x77a, 1, 0x7df, 1);
        if(ret == 0)
        {
            app.log_text("Create Diagnostic Success, module handle",lvlInfo);
            TestStep("step:tsdiag_can_create","tsdiag_can_create ok");
        }
        else
        {
            app.log_text("Create Diagnostic Failed",lvlError);
            TestStep("step:tsdiag_can_create","tsdiag_can_create failed");
            return ret;
        }
        app.wait(1000,"");
        TestStep("step:send 1001","send 1001");
        u8 reqDataArray[]= {0x10,0x03};
        s32 reqDataSize = sizeof(reqDataArray);
        u8 responseArray[10] = {0};             // 准备一个 10 字节的接收缓冲区并清零
        s32 responseDataSize = 10;              // 告诉函数：我的缓冲区最大是 10 字节
        ret = rtlUIDiagnostics.tstp_can_request_and_get_response(
            udsHandle,          // 诊断模块/句柄索引 (s32)
            reqDataArray,       // 请求数据指针 (pu8)
            reqDataSize,        // 请求数据长度 (s32)
            responseArray,      // 接收响应的缓冲区指针 (pu8)
            &responseDataSize   // 接收响应实际长度的指针 (ps32)
        );
        if (ret == 0) {
            TestStepPass("step:send 1001","send 1001 ok");
        } else {
            TestStepFail("step:send 1001","send 1001 failed");
        }
        // test_final();
        return IDX_ERR_OK;
            
    }
    catch(...)
    {
        return IDX_ERR_MP_CODE_CRASH;
    }
}

