# ece386-lab01

Serving handwritten digit inference with FastAPI.

See [USAFA ECE 386: AI Hardware Applications - Lab 1](https://usafa-ece.github.io/ece386-book/b1-prediction/lab-digits-api.html)


## Writeup

What strategies did you use to ensure that your client and server were communicating with the same schema?
We used the pillow library to sanitize our images. We use ImageOps.grayscale() & img = img.resize((28,28)) to ensure that the images being sent to the model were in the right format. 

In regard to preprocesing your digit images, how well do you think your server would scale to *any* picture of a digit?
I think that resizing any image may not be optimal for the model. To start, it would not work well with images that are not white on a black background or not png files. If the image is square, I forsee that it would scale relatively well; however, if it is not than the scaling may impact the image. For example, we put in an example image of a 9, but the file was rectangular. When we ran it through the model, it was squished on the x axis, causing the model to interpret it as a 1.

Does the client/server architecture make sense for this problem? Why or why not?
I would say that the client/server architecture makes sense so that the host computer does not need to have the model. Additionally, the processing is done off computer, which allows for the deep neural network to run on computers with minimal hardware. It also allows for the project to scale and provide more application while the client side process can remain relatively constant.

## Documentation

*Documentation statement. Pay special attention to the LLM policy.*

https://fastapi.tiangolo.com/tutorial/ for how to use FastAPI.
https://www.w3schools.com/python/ref_requests_post.asp for post request to the server
https://www.geeksforgeeks.org/python-pil-tobytes-method/ for getting the image bytes from the image path
https://www.geeksforgeeks.org/python-pil-imageops-greyscale-method/ for grayscaling image
https://www.geeksforgeeks.org/python-pil-image-resize-method/ for resizing image
