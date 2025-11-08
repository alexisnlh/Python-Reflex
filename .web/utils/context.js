import { createContext } from "react"
import { E } from "/utils/state.js"

export const initialState = {"chat_history": [], "is_hydrated": false, "question": ""}
export const initialEvents = [E('state.hydrate', {})]
export const StateContext = createContext(null);
export const EventLoopContext = createContext(null);