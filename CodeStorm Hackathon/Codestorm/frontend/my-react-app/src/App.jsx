import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import { useSelector } from "react-redux";
import Spinner from "./components/Spinner";
import ProtectedRoute from "./components/ProtectedRoute";
import PublicRoute from "./components/PublicRoute";

import Header from "./pages/Header";
import DashboardTemplate from "./pages/DashboardTemplate";
import Application from "./pages/Application";

import Apply from "./pages/Apply";
import Difficulties from "./pages/Difficulties";
import Address from "./pages/Address";

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BrowserRouter>
        { (
          <Routes>
            <Route
              path="/"
              element={
                  <><Header /><DashboardTemplate /></>
              }
            />
            <Route
              path="/jobs"
              element={
                  <><Header /><Apply /><DashboardTemplate /></>
              }
            />
            <Route
              path="/login"
              element={
                <PublicRoute>
                  <Login />
                </PublicRoute>
              }
            />
            <Route
              path="/register"
              element={
                <PublicRoute>
                  <Register />
                </PublicRoute>
              }
            />
            <Route
              path="/application"
              element={
                <><Header /><Application /><DashboardTemplate /></>
                
              }
            />
            <Route
              path="/diff"
              element={
                  <><Header /><Difficulties /><DashboardTemplate /></>
              }
            />
            <Route
              path="/address"
              element={
                  <><Header /><Address /><DashboardTemplate /></>
              }
            />
          </Routes>
        )}
      </BrowserRouter>
    </>
  )
}

export default App
