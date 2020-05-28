# init python:
#     import jnius
#     PythonSDLActivity = jnius.autoclass("org.renpy.android.PythonSDLActivity")

# python:
#     PythonSDLActivity.myStaticMethod(1, 2, "Flan")

# This is the JAVA CODE to send an image, from
#  https://developer.android.com/training/sharing/send#java
# 
#     Intent shareIntent = new Intent();
#     shareIntent.setAction(Intent.ACTION_SEND);
#     shareIntent.putExtra(Intent.EXTRA_STREAM, uriToImage);
#     shareIntent.setType("image/jpeg");
#     startActivity(Intent.createChooser(shareIntent, getResources().getText(R.string.send_to)));

init python:
    if renpy.android:

        def shareImageAndroid():
            import jnius

            # import the needed Java class
            PythonActivity = autoclass('org.renpy.android.PythonActivity') #SDLActivity?
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')

            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('http://metasepiagames.com/PluginPoetry'))

            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our
            # PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)

            # The website will open.
            return