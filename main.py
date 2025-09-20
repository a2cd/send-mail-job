import os
from loguru import logger
from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    logger.info("定时任务执行！")


if __name__ == "__main__":
    # 日志目录
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    os.makedirs(log_dir, exist_ok=True)

    # remove the default handler configuration
    logger.remove()
    # 配置Loguru日志：每分钟新建，保留7天
    logger.add(
        "logs/job-{time:YYYYMMDD}.log",
        rotation="00:00",
        retention="7 days",
        encoding="utf-8",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> - [<level>{level}</level>]: {message}",
    )

    # 启动定时任务
    scheduler = BlockingScheduler()
    scheduler.add_job(job, "interval", seconds=5)  # 每60秒执行一次
    scheduler.start()
