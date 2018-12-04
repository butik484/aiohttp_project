from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task(12)
    def get_status(self):
        self.client.get('/status')

    @task(25)
    def get_lowcost(self):
        self.client.get('/lower')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
