"""
Medicinal Plant Identification App using Gemini AI
Upload a plant image to identify it and learn about its medicinal uses
"""

import gradio as gr
import google.generativeai as genai
from PIL import Image
import os
import base64
import io

class MedicinalPlantIdentifier:
    def __init__(self, api_key):
        """Initialize the Gemini AI model"""
        self.api_key = api_key
        genai.configure(api_key=api_key)
        
        # Initialize the Gemini Pro Vision model
        self.model = genai.GenerativeModel('gemini-2.5-flash-lite')
        
    def identify_plant(self, image):
        """Identify medicinal plant and provide information about its uses"""
        try:
            if image is None:
                return "❌ Please upload an image first!"
            
            # Prepare the prompt for plant identification
            prompt = """
            You are an expert botanist and herbalist. Please analyze this plant image and provide:

            1. **Plant Identification**: 
               - Scientific name (if identifiable)
               - Common name(s)
               - Plant family
               - Confidence level of identification

            2. **Medicinal Uses**:
               - Traditional medicinal uses
               - Active compounds (if known)
               - Parts of plant used (leaves, roots, flowers, etc.)
               - Preparation methods (tea, extract, paste, etc.)

            3. **Safety Information**:
               - Any known side effects or precautions
               - Dosage recommendations (if applicable)
               - Contraindications

            4. **Additional Information**:
               - Geographic distribution
               - Growing conditions
               - Harvesting tips

            Please format your response clearly with emojis and be comprehensive but easy to understand. If you cannot identify the plant with confidence, please state that clearly and provide general safety advice about unknown plants.

            IMPORTANT: Always include a disclaimer about consulting healthcare professionals before using any plant medicinally.
            """
            
            # Generate response using Gemini
            response = self.model.generate_content([prompt, image])
            
            if response and response.text:
                # Format the response nicely
                formatted_response = self._format_response(response.text)
                return formatted_response
            else:
                return "❌ Sorry, I couldn't analyze this image. Please try with a clearer plant image."
                
        except Exception as e:
            return f"❌ Error occurred during analysis: {str(e)}\n\nPlease check your internet connection and try again."
    
    def _format_response(self, text):
        """Format the AI response for better readability"""
        # Add header
        formatted = "🌿 **MEDICINAL PLANT ANALYSIS RESULTS** 🌿\n\n"
        formatted += text
        formatted += "\n\n" + "⚠️" * 3 + " **IMPORTANT DISCLAIMER** " + "⚠️" * 3
        formatted += "\n\n🏥 **Always consult with qualified healthcare professionals before using any plant for medicinal purposes. This information is for educational purposes only and should not replace professional medical advice.**"
        
        return formatted

def create_interface():
    """Create the Gradio interface"""
    
    # Initialize the plant identifier
    api_key = "AIzaSyA8MCifwTI_KaCZQjF9S14SOqCTvblii3Y"
    identifier = MedicinalPlantIdentifier(api_key)
    
    # Create the interface
    interface = gr.Interface(
        fn=identifier.identify_plant,
        inputs=[
            gr.Image(
                type="pil",
                label="📸 Upload Plant Image"
            )
        ],
        outputs=[
            gr.Textbox(
                label="🌿 Plant Analysis & Medicinal Uses",
                info="AI-powered plant identification and medicinal information",
                lines=20,
                max_lines=30
            )
        ],
        title="🌿 Medicinal Plant Identifier & Uses Guide 🌿",
        description="""
        **Upload an image of a medicinal plant to:**
        - 🔍 **Identify** the plant species
        - 💊 **Learn** about its medicinal uses
        - ⚗️ **Discover** preparation methods
        - ⚠️ **Understand** safety precautions
        
        **Powered by Google Gemini AI** for accurate plant identification and comprehensive medicinal information.
        
        📋 **Tips for best results:**
        - Use clear, well-lit photos
        - Include leaves, flowers, or distinctive features
        - Avoid blurry or distant shots
        """,
        article="""
        ### 🌟 About This App
        
        This application uses advanced AI to identify medicinal plants and provide detailed information about their traditional and modern uses. 
        
        ### 🔬 What You'll Learn:
        - **Scientific identification** of the plant
        - **Traditional medicinal uses** across cultures
        - **Active compounds** and their effects
        - **Preparation methods** for different applications
        - **Safety information** and precautions
        
        ### ⚠️ Important Notes:
        - This tool is for **educational purposes only**
        - Always **consult healthcare professionals** before using plants medicinally
        - **Never consume unknown plants** without expert verification
        - Some plants can be **toxic or harmful** if misused
        
        ### 🌍 Supporting Traditional Knowledge
        This app helps preserve and share traditional botanical knowledge while promoting safe, informed use of medicinal plants.
        """,
        theme="soft",
        examples=[
            # We can add example images here if needed
        ],
        flagging_mode="never"
    )
    
    return interface

def main():
    """Launch the application"""
    print("🌿 Starting Medicinal Plant Identifier App...")
    print("🔗 Powered by Google Gemini AI")
    
    # Create and launch interface
    interface = create_interface()
    
    # Launch interface with public sharing
    interface.launch(share=True)

if __name__ == "__main__":
    main()