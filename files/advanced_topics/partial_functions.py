from functools import partial

class ImageProcessor:
    def apply_filter(self, image, filter_type='blur', intensity=1):
        # Mock implementation of applying a filter
        return f"Applied {filter_type} filter with intensity {intensity} on {image}"

# Create an instance of ImageProcessor
processor = ImageProcessor()

# Partial function for applying a 'sharpen' filter with intensity 3
sharpen_filter = partial(processor.apply_filter, filter_type='sharpen', intensity=3)

# Apply the sharpen filter on an image
result = sharpen_filter("image1.png")
print(result)  # Output: Applied sharpen filter with intensity 3 on image1.png


# --------------------------------------------------
# Example transformation functions
def scale(value, factor=1):
    return value * factor

def offset(value, amount=0):
    return value + amount

def clip(value, min_value=0, max_value=100):
    return max(min_value, min(value, max_value))

# Create partial functions for specific transformations
scale_by_10 = partial(scale, factor=10)
offset_by_5 = partial(offset, amount=5)
clip_to_0_50 = partial(clip, min_value=0, max_value=50)

# Data processing pipeline
data = [1, 2, 3, 4, 5, 100]

# Apply transformations
processed_data = list(map(clip_to_0_50, map(offset_by_5, map(scale_by_10, data))))

print(processed_data)  # Output: [15, 25, 35, 45, 50, 50]
