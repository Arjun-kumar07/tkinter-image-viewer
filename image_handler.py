from PIL import Image, ImageTk

class ImageHandler:
    
    def resize_image(self, image):

        # Use the original aspect ratio of the image to resize
        if image.height > 300:
            aspect_ratio = image.width / image.height
            new_width = aspect_ratio * 300
            return image.resize((int(new_width), 300), Image.Resampling.LANCZOS)

        if image.width > 500:
            aspect_ratio = image.width / image.height
            new_height = 500 * aspect_ratio
            return image.resize((500, int(new_height)), Image.Resampling.LANCZOS)

        return image
    
    def display_image(self):

        try:
            self.name_label.configure(text=self.image_files[self.current_image_index])
            new_img = Image.open(f"{self.img_dir}/{self.image_files[self.current_image_index]}")
            self.current_image = ImageTk.PhotoImage(self.resize_image(new_img))
            self.display.configure(image=self.current_image)

        except OSError as e:
            self.name_label.configure(text=e)
            self.current_image = ImageTk.PhotoImage(self.blank_img)
            self.display.configure(image=self.current_image)

        except IndexError:
            self.name_label.configure(text="No image files found")
            self.current_image = ImageTk.PhotoImage(self.blank_img)
            self.display.configure(image=self.current_image)
            
            
    