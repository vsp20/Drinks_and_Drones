const restClient = require("./restClient")
// @ponicode
describe("restClient.default", () => {
    test("0", () => {
        let param3 = [["https://accounts.google.com/o/oauth2/revoke?token=%s", "https://croplands.org/app/a/reset?token=", "https://croplands.org/app/a/reset?token="], ["http://www.example.com/route/123?foo=bar", "https://croplands.org/app/a/confirm?t=", "https://accounts.google.com/o/oauth2/revoke?token=%s"], ["http://www.croplands.org/account/confirm?t=", "www.google.com", "https://api.telegram.org/"]]
        let callFunction = () => {
            restClient.default(["object", "number", "string"], "deposit transaction at Streich, Mann and Rutherford using card ending with ***5156 for TJS 69.36 in account ***97846125", param3)
        }
    
        expect(callFunction).not.toThrow()
    })

    test("1", () => {
        let param3 = [["http://www.croplands.org/account/confirm?t=", "https://accounts.google.com/o/oauth2/revoke?token=%s", "ponicode.com"], ["https://api.telegram.org/bot", "http://www.example.com/route/123?foo=bar", "http://www.croplands.org/account/confirm?t="], ["http://www.croplands.org/account/confirm?t=", "http://www.croplands.org/account/confirm?t=", "https://"]]
        let callFunction = () => {
            restClient.default(["array", "array", "object"], "withdrawal transaction at Kovacek Inc using card ending with ***6291 for IRR 718.83 in account ***77705372", param3)
        }
    
        expect(callFunction).not.toThrow()
    })

    test("2", () => {
        let param3 = [["Www.GooGle.com", "https://", "https://twitter.com/path?abc"], ["https://accounts.google.com/o/oauth2/revoke?token=%s", "ponicode.com", "ponicode.com"], ["www.google.com", "www.google.com", "https://"]]
        let callFunction = () => {
            restClient.default(["array", "object", "array"], "withdrawal transaction at Kovacek Inc using card ending with ***6291 for IRR 718.83 in account ***77705372", param3)
        }
    
        expect(callFunction).not.toThrow()
    })

    test("3", () => {
        let param3 = [["ponicode.com", "https://accounts.google.com/o/oauth2/revoke?token=%s", "ponicode.com"], ["https://twitter.com/path?abc", "http://base.com", "www.google.com"], ["https://twitter.com/path?abc", "https://accounts.google.com/o/oauth2/revoke?token=%s", "http://example.com/showcalendar.html?token=CKF50YzIHxCTKMAg"]]
        let callFunction = () => {
            restClient.default(["number", "array", "string"], "payment transaction at Satterfield - Hyatt using card ending with ***0494 for GHS 370.23 in account ***63108447", param3)
        }
    
        expect(callFunction).not.toThrow()
    })

    test("4", () => {
        let param3 = [["https://croplands.org/app/a/reset?token=", "https://api.telegram.org/", "https://croplands.org/app/a/reset?token="], ["https://api.telegram.org/", "http://example.com/showcalendar.html?token=CKF50YzIHxCTKMAg", "http://base.com"], ["https://", "http://example.com/showcalendar.html?token=CKF50YzIHxCTKMAg", "ponicode.com"]]
        let callFunction = () => {
            restClient.default(["number", "array", "array"], "withdrawal transaction at Kovacek Inc using card ending with ***6291 for IRR 718.83 in account ***77705372", param3)
        }
    
        expect(callFunction).not.toThrow()
    })

    test("5", () => {
        let callFunction = () => {
            restClient.default(undefined, undefined, [])
        }
    
        expect(callFunction).not.toThrow()
    })
})
