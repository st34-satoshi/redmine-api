from redminelib import Redmine
from redminelib.exceptions import ResourceNotFoundError


def print_all_ticket():
    try:
        redmine = Redmine('url', key='token_key')
        issues = redmine.issue.all(sort='category:desc')
        for issue in issues:
              print ('%d:%s' % (issue.id, issue.subject, issue.project_id))

    except (ResourceNotFoundError):
        print(ResourceNotFoundError)
        # print("Not found {0}".format(issue))


def create_issue():
    try:
        redmine = Redmine('url', key='token_key')
        issue = redmine.issue.new()
        issue.project_id = 'id'
        issue.subject = 'タイトル！'
        # issue.tracker_id = 1  # トラッカー
        issue.description = 'ST botにより作成されました。'
        # issue.status_id = 1  # ステータス
        # issue.priority_id = 1  # 優先度
        # issue.assigned_to_id = 1  # 担当者のID
        # # issue.watcher_user_ids = [1, 3]  # ウォッチするユーザのID
        # # issue.parent_issue_id = 12  # 親チケットのID
        # issue.start_date = datetime.date(2019, 10, 19)  # 開始日
        # issue.due_date = datetime.date(2019, 10, 20)  # 期日
        # issue.estimated_hours = 4  # 予想工数
        # issue.done_ratio = 40
        # issue.custom_fields = [{'id': 1, 'value': 'foo'}]
        # # issue.uploads = [{'path': '/share/test.txt'}]
        # issue.uploads = [{'path': '/main.py'}]
        issue.save()

    except (ResourceNotFoundError):
        print(ResourceNotFoundError)
        # print("Not found {0}".format(issue))

if __name__ == '__main__':
    print_all_ticket()
