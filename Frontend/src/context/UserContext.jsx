import { createContext, useState, useEffect } from "react";

export const UserContext = createContext({});

export function UserContextProvider({ children }) {
  const [userInfo, setUserInfo] = useState(null);

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        const response = await fetch(
          "https://predictix.onrender.com/api/v1/users/profile",
          {
            credentials: "include", // Sends cookies with the request
          }
        );

        if (response.ok) {
          const userData = await response.json();
          setUserInfo(userData); // Set user info in context
        } else {
          setUserInfo(null); // Clear user info if not authenticated
        }
      } catch (error) {
        console.error("Failed to fetch user profile:", error);
        setUserInfo(null);
      }
    };

    fetchUserProfile();
  }, []);

  return (
    <UserContext.Provider value={{ userInfo, setUserInfo }}>
      {children}
    </UserContext.Provider>
  );
}
