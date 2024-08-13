# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-06-23 14:48:36
@LastEditTime : 2020-08-12 10:10:39
@LastEditors  : yi.mt
@Description  : 
'''

realm = {
    "roles": {},
    "rules": {
    }
}

ware = {
    "init_task_stages": ("""INSERT IGNORE INTO task.t_TaskStage(TaskID, RunID, StageID, StageTag, StageName, UpdateDate, UpdateTime, Status, Remark)
                                VALUES(#{taskID}, #{runID}, #{stageID}, #{stageTag}, #{stageName}, DATE_FORMAT(NOW(), '%Y%m%d'), DATE_FORMAT(NOW(), '%H:%i:%S'), #{stageStatus}, #{stageRemark})""", {"many": True}),
    "clean_task_stages": ("""DELETE FROM task.t_TaskStage WHERE TaskID = #{taskID} AND RunID = #{runID} AND StageID = #{stageID}""", {"many": True}),
    "mark_task_stage": ("""UPDATE task.t_TaskStage
                                SET UpdateDate = DATE_FORMAT(NOW(), '%Y%m%d'), UpdateTime = DATE_FORMAT(NOW(), '%H:%i:%S'), StageTag = #{stageTag}, Status = #{stageStatus}, Remark = #{stageRemark}
                                WHERE TaskID = #{taskID} AND RunID = #{runID} AND StageID = #{stageID}""", {"return": True}),
    "get_task_stage_status": """SELECT STATUS FROM task.t_TaskStage WHERE TaskID = #{taskID} AND RunID = #{runID} AND StageID = #{stageID}""",
    "init_task_procedures": ("""INSERT IGNORE INTO task.t_TaskProcedure(TaskID, RunID, StageID, StageTag, ProcedureID, ProcedureName, UpdateDate, UpdateTime, Status, Remark)
                                    VALUES(#{taskID}, #{runID}, #{stageID}, #{stageTag}, #{procedureID}, #{procedureName}, DATE_FORMAT(NOW(), '%Y%m%d'), DATE_FORMAT(NOW(), '%H:%i:%S'), #{procedureStatus}, #{procedureRemark})""", {"many": True}),
    "clean_task_procedures": ("""DELETE FROM task.t_TaskProcedure WHERE TaskID = #{taskID} AND RunID = #{runID} AND StageID = #{stageID}""", {"many": True}),
    "mark_task_procedure": ("""UPDATE task.t_TaskProcedure
                                SET UpdateDate = DATE_FORMAT(NOW(), '%Y%m%d'), UpdateTime = DATE_FORMAT(NOW(), '%H:%i:%S'), StageTag = #{stageTag}, Status = #{procedureStatus}, Remark = #{procedureRemark}
                                WHERE TaskID = #{taskID} And RunID = #{runID} AND StageID = #{stageID} AND ProcedureID = #{procedureID}""", {"return": True}),
    "get_task_procedure_status": """SELECT STATUS FROM task.t_TaskProcedure WHERE TaskID = #{taskID} AND RunID = #{runID} AND StageID = #{stageID} AND ProcedureID = #{procedureID}""",
    
};