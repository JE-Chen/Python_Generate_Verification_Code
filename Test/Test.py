from JEVerificationCode.Core import VerificationCodeCore

g = VerificationCodeCore()
Code = g.GenerateVerificationCode.generate_base64_image(True)
print(Code[0])
print(Code[1])

print(g.GenerateVerificationCode.generate_code_only_string(5))
