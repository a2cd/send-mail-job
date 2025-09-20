from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print("定时任务执行！")


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(job, "interval", seconds=5)  # 每5秒执行一次
    scheduler.start()
