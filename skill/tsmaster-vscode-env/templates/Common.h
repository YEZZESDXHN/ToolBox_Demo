#ifndef __COMMON_H
#define __COMMON_H

#include "TSMaster.h"
#include "MPLibrary.h"

// 声明全局变量，TSMaster 会在 TSMaster_Entry.cpp 的初始化函数中填充它们
extern TTSApp app;
extern TTSCOM com;
extern TTSTest test;

extern native_int report_handle;
extern Ttest_report test_report;
extern TrtlUIDiagnostics rtlUIDiagnostics;
extern s32 diag_module_index;

// 在此处定义can发送/接收，变量变化等各种TSMaster的回调函数，会在 TSMaster_Entry.cpp 的初始化函数中填充它们
extern void step(void);
extern void on_can_rx_NewOn_CAN_Rx1(const TCAN* ACAN);
extern void on_canfd_rx_NewOn_CAN_FD_Rx1(const TCANFD* ACANFD);
extern void on_can_tx_NewOn_CAN_Tx1(const TCAN* ACAN);
extern void on_canfd_tx_NewOn_CAN_FD_Tx1(const TCANFD* ACANFD);
extern void on_can_pretx_NewOn_CAN_PreTx1(const PCAN ACAN);
extern void on_canfd_pretx_NewOn_CAN_FD_PreTx1(const PCANFD ACANFD);
extern void on_lin_rx_NewOn_LIN_Rx1(const TLIN* ALIN);
extern void on_lin_tx_NewOn_LIN_Tx1(const TLIN* ALIN);
extern void on_lin_pretx_NewOn_LIN_PreTx1(const PLIN ALIN);
extern void on_var_change_NewOn_Var_Change1(void);
extern void on_timer_NewOn_Timer1(void);
extern void on_timer_group_NewOn_Timer_Group1(const s32 AIndex);
extern void on_start_NewOn_Start1(void);
extern void on_stop_NewOn_Stop1(void);
extern void on_shortcut_NewOn_Shortcut1(const s32 AShortcut);




extern TMPTimerMSUpg1 NewTimer1;
extern TMPTimerMsGroup NewTimer_Group1;


#endif
