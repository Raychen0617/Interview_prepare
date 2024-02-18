# Background

## CT MRI Volume Rendering

[Getting Started with Volume Rendering using OpenGL - CodeProject](https://www.codeproject.com/Articles/352270/Getting-Started-with-Volume-Rendering-using-OpenGL)

1. Store multiple textures with different z axis.
2. Do transparency, set alpha to 0 for some points that have alpha smaller than the threshold
3. Do blending and disable depth test.

Rotation issue

- when the model is rotating by z axis, 上下顛倒
- when the model is rotating 90 or 270 degree, the image wil disappear since there are no enough textures