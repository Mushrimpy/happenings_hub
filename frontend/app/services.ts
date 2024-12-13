export async function signUp(userData: any) {
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/auth/signup`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });
  
      if (!response.ok) {
        throw new Error("Failed to sign up. Please check your information.");
      }
  
      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Sign-up error:", error);
      throw error;
    }
  }