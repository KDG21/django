from django.views import View
from django.http import JsonResponse, HttpResponse
from pose.pose_engine import Pose_Check
from django.core.files.storage import default_storage

class PoseCheckView(View):
    def post(self, request):
        video_file = request.FILES['file']
        default_storage.save(video_file.name, video_file)

        pose_json = Pose_Check.pose_run(self, video_file.name)

        # return HttpResponse(status=200)
        return JsonResponse({'pose_json' : pose_json}, status=200)